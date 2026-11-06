
# Ascendor API Specification

## MVP Lead Intake API

### Endpoint
POST /api/v1/leads

### Purpose
Receive and process incoming business leads.

### Request Body
```json
{
  "name": "John Smith",
  "email": "john@example.com",
  "phone": "+639123456789",
  "company": "Example Company",
  "source": "website"
}
```

### Successful Response
HTTP 201 Created

```json
{
  "success": true,
  "message": "Lead created successfully",
  "lead_id": "generated-uuid"
}
```

### Duplicate Response
HTTP 409 Conflict

### Validation Error
HTTP 400 Bad Request

### Internal Server Error
HTTP 500 Internal Server Error
