
-- ==========================================
-- ASCENDOR MVP
-- Initial PostgreSQL Database Schema
-- ==========================================

CREATE TABLE IF NOT EXISTS leads (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    full_name VARCHAR(150) NOT NULL,

    email VARCHAR(254) NOT NULL,

    phone VARCHAR(30),

    source VARCHAR(100) NOT NULL DEFAULT 'webhook',

    status VARCHAR(30) NOT NULL DEFAULT 'NEW',

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT leads_status_check
        CHECK (
            status IN (
                'NEW',
                'QUALIFIED',
                'UNQUALIFIED',
                'CONTACTED',
                'CONVERTED'
            )
        )
);

-- Index for email-based lead lookup
CREATE INDEX IF NOT EXISTS idx_leads_email
    ON leads (LOWER(email));

-- Index for lead status filtering
CREATE INDEX IF NOT EXISTS idx_leads_status
    ON leads (status);

-- Index for chronological lead retrieval
CREATE INDEX IF NOT EXISTS idx_leads_created_at
    ON leads (created_at DESC);
