-- ==========================================
-- ASCENDOR LEAD-TO-REVENUE ENGINE
-- MVP DATABASE SCHEMA
-- ==========================================

CREATE TABLE IF NOT EXISTS leads (
id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

full_name VARCHAR(150) NOT NULL,

email VARCHAR(254) NOT NULL,

phone VARCHAR(30),

company_name VARCHAR(150),

source VARCHAR(100) NOT NULL DEFAULT 'webhook',

status VARCHAR(30) NOT NULL DEFAULT 'NEW',

lead_score INTEGER NOT NULL DEFAULT 0,

qualification_status VARCHAR(30)
    NOT NULL DEFAULT 'PENDING',

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

CONSTRAINT leads_score_check
    CHECK (lead_score BETWEEN 0 AND 100),

CONSTRAINT leads_qualification_check
    CHECK (
        qualification_status IN (
            'PENDING',
            'QUALIFIED',
            'UNQUALIFIED'
        )
    ),

CONSTRAINT leads_estimated_revenue_check
    CHECK (estimated_revenue IS NULL OR estimated_revenue >= 0),

CONSTRAINT leads_actual_revenue_check
    CHECK (actual_revenue IS NULL OR actual_revenue >= 0)

);

-- Normalize email addresses automatically
CREATE OR REPLACE FUNCTION normalize_lead_email()
RETURNS TRIGGER AS $$
BEGIN
NEW.email := LOWER(TRIM(NEW.email));
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_normalize_lead_email
BEFORE INSERT OR UPDATE OF email ON leads
FOR EACH ROW
EXECUTE FUNCTION normalize_lead_email();

-- Prevent duplicate emails regardless of letter casing
CREATE UNIQUE INDEX IF NOT EXISTS idx_leads_email_unique
ON leads (LOWER(email));

-- Automatically update updated_at
CREATE OR REPLACE FUNCTION update_lead_timestamp()
RETURNS TRIGGER AS $$
BEGIN
NEW.updated_at := NOW();
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_lead_timestamp
BEFORE UPDATE ON leads
FOR EACH ROW
EXECUTE FUNCTION update_lead_timestamp();

-- Performance indexes
CREATE INDEX IF NOT EXISTS idx_leads_status
ON leads (status);

CREATE INDEX IF NOT EXISTS idx_leads_created_at
ON leads (created_at DESC);

CREATE INDEX IF NOT EXISTS idx_leads_score
ON leads (lead_score DESC);