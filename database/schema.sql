-- ============================================================
-- ASCENDOR LEAD-TO-REVENUE ENGINE
-- MVP DATABASE SCHEMA
-- PostgreSQL
-- ============================================================

-- ============================================================
-- 1. LEADS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS leads (
id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

full_name VARCHAR(150) NOT NULL,
email VARCHAR(254) NOT NULL,
phone VARCHAR(30),
company_name VARCHAR(150),

source VARCHAR(100) NOT NULL DEFAULT 'webhook',

status VARCHAR(30) NOT NULL DEFAULT 'NEW',

qualification_status VARCHAR(30)
    NOT NULL DEFAULT 'PENDING',

lead_score INTEGER NOT NULL DEFAULT 0,

estimated_revenue NUMERIC(12,2),
actual_revenue NUMERIC(12,2),

converted_at TIMESTAMPTZ,

created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

CONSTRAINT leads_status_check
    CHECK (
        status IN (
            'NEW',
            'QUALIFIED',
            'UNQUALIFIED',
            'CONTACTED',
            'CONVERTED',
            'LOST'
        )
    ),

CONSTRAINT leads_qualification_check
    CHECK (
        qualification_status IN (
            'PENDING',
            'QUALIFIED',
            'UNQUALIFIED'
        )
    ),

CONSTRAINT leads_score_check
    CHECK (lead_score BETWEEN 0 AND 100),

CONSTRAINT leads_estimated_revenue_check
    CHECK (
        estimated_revenue IS NULL
        OR estimated_revenue >= 0
    ),

CONSTRAINT leads_actual_revenue_check
    CHECK (
        actual_revenue IS NULL
        OR actual_revenue >= 0
    ),

CONSTRAINT leads_conversion_check
    CHECK (
        status <> 'CONVERTED'
        OR converted_at IS NOT NULL
    )

);

-- ============================================================
-- 2. EMAIL NORMALIZATION
-- ============================================================

CREATE OR REPLACE FUNCTION normalize_lead_email()
RETURNS TRIGGER AS $$
BEGIN
NEW.email := LOWER(TRIM(NEW.email));
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_normalize_lead_email ON leads;

CREATE TRIGGER trg_normalize_lead_email
BEFORE INSERT OR UPDATE OF email ON leads
FOR EACH ROW
EXECUTE FUNCTION normalize_lead_email();

-- ============================================================
-- 3. DUPLICATE EMAIL PREVENTION
-- ============================================================

CREATE UNIQUE INDEX IF NOT EXISTS idx_leads_email_unique
ON leads (LOWER(email));

-- ============================================================
-- 4. AUTOMATIC UPDATED_AT
-- ============================================================

CREATE OR REPLACE FUNCTION update_lead_timestamp()
RETURNS TRIGGER AS $$
BEGIN
NEW.updated_at := NOW();
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_update_lead_timestamp ON leads;

CREATE TRIGGER trg_update_lead_timestamp
BEFORE UPDATE ON leads
FOR EACH ROW
EXECUTE FUNCTION update_lead_timestamp();

-- ============================================================
-- 5. LEAD ACTIVITY HISTORY
-- ============================================================

CREATE TABLE IF NOT EXISTS lead_activities (
id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

lead_id UUID NOT NULL
    REFERENCES leads(id)
    ON DELETE CASCADE,

activity_type VARCHAR(50) NOT NULL,

description TEXT NOT NULL,

metadata JSONB NOT NULL DEFAULT '{}'::JSONB,

created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()

);

-- ============================================================
-- 6. FOLLOW-UP TRACKING
-- ============================================================

CREATE TABLE IF NOT EXISTS lead_followups (
id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

lead_id UUID NOT NULL
    REFERENCES leads(id)
    ON DELETE CASCADE,

followup_type VARCHAR(50) NOT NULL DEFAULT 'EMAIL',

scheduled_at TIMESTAMPTZ NOT NULL,

completed_at TIMESTAMPTZ,

status VARCHAR(30) NOT NULL DEFAULT 'PENDING',

attempts INTEGER NOT NULL DEFAULT 0,

last_error TEXT,

created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

CONSTRAINT followups_status_check
    CHECK (
        status IN (
            'PENDING',
            'PROCESSING',
            'COMPLETED',
            'FAILED',
            'CANCELLED'
        )
    ),

CONSTRAINT followups_attempts_check
    CHECK (attempts >= 0)

);

-- ============================================================
-- 7. PERFORMANCE INDEXES
-- ============================================================

CREATE INDEX IF NOT EXISTS idx_leads_status
ON leads(status);

CREATE INDEX IF NOT EXISTS idx_leads_created_at
ON leads(created_at DESC);

CREATE INDEX IF NOT EXISTS idx_leads_score
ON leads(lead_score DESC);

CREATE INDEX IF NOT EXISTS idx_lead_activities_lead_id
ON lead_activities(lead_id);

CREATE INDEX IF NOT EXISTS idx_lead_activities_created_at
ON lead_activities(created_at DESC);

CREATE INDEX IF NOT EXISTS idx_followups_scheduled
ON lead_followups(scheduled_at)
WHERE status = 'PENDING';

CREATE INDEX IF NOT EXISTS idx_followups_lead_id
ON lead_followups(lead_id);

-- ============================================================
-- END OF ASCENDOR MVP DATABASE SCHEMA
-- ============================================================