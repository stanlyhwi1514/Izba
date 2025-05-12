breifing_document_schema ={
    
  "title": "Briefing Schema",
  "type": "object",
  "required": [
    "customer_id",
    "title",
    "account_name",
    "description",
    "fiscal_year",
    "status",
    "generated_on",
    "arr_summary",
    "new_opportunities",
    "tags",
    "relationships",
    "zappy_response",
    "sentiment_image_url",
    "created_at",
    "updated_at",
    "bookmarks",
    "drafts",
    "saved",
    "document_name"

  ],
  "properties": {
    "document_name": { "type": "string" },
    "bookmarks": { "type": "boolean" },
    "drafts": { "type": "boolean" },
    "saved": { "type": "boolean" },
    "customer_id": { "type": "string" },
    "title": { "type": "string" },
    "sign_off_by": { "type": "string" },
    "account_name": { "type": "string" },
    "description": { "type": "string" },
    "fiscal_year": {
      "type": "string",
      "pattern": "^FY\\d{2}$"
    },
    "status": {
      "type": "string",
      "enum": ["Live", "Draft", "Archived"]
    },
    "generated_on": {
      "type": "string",
      "format": "date-time"
    },
    "arr_summary": {
      "type": "object",
      "required": ["start_date", "renewal_date", "amount"],
      "properties": {
        "start_date": {
          "type": "string",
          "format": "date-time"
        },
        "renewal_date": {
          "type": "string",
          "format": "date-time"
        },
        "amount": {
          "type": "number",
          "minimum": 0
        }
      }
    },
    "new_opportunities": {
      "type": "object",
      "required": ["project_close", "amount"],
      "properties": {
        "project_close": {
          "type": "string",
          "format": "date-time"
        },
        "amount": {
          "type": "number",
          "minimum": 0
        }
      }
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1
    },
    "relationships": {
      "type": "object",
      "required": ["customer_contacts", "vendor_contacts"],
      "properties": {
        "customer_contacts": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["name", "role"],
            "properties": {
              "name": { "type": "string" },
              "role": { "type": "string" }
            }
          }
        },
        "vendor_contacts": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["name", "role"],
            "properties": {
              "name": { "type": "string" },
              "role": { "type": "string" }
            }
          }
        }
      }
    },
    "zappy_response": { "type": "string" },
    "sentiment_image_url": {
      "type": "string",
      "format": "uri"
    },
    "Risks": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "severity", "raised_by", "content", "source", "date", "current_status"],
        "properties": {
          "type": { "type": "string" },
          "severity": { "type": "string" },
          "raised_by": { "type": "string" },
          "content": { "type": "string" },
          "source": { "type": "string", "format": "uri" },
          "date": { "type": "string" },
          "current_status": {
            "type": "string",
            "enum": ["playbook activated", "new", "validated"]
          }
        }
      }
    },
    "Opportunities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "severity", "raised_by", "content", "source", "date", "current_status"],
        "properties": {
          "type": { "type": "string" },
          "severity": { "type": "string" },
          "raised_by": { "type": "string" },
          "content": { "type": "string" },
          "source": { "type": "string", "format": "uri" },
          "date": { "type": "string" },
          "current_status": {
            "type": "string",
            "enum": ["playbook activated", "new", "validated"]
          }
        }
      }
        },
    "playbooks": {
      "type": "object",
      "properties": {
        "unsuccessful": { "type": "number" },
        "active": { "type": "number" },
        "list": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "play_book_name": { "type": "string" },
              "customer_name": { "type": "string" },
              "date": {
                "type": "string",
                "pattern": "^(0[1-9]|[12][0-9]|3[01])/([0][1-9]|1[0-2])/([0-9]{4})$"
              },
              "owning_percentage": {
                "type": "string",
                "pattern": "^(100|[1-9]?[0-9])%$"
              }
            },
            "required": ["play_book_name", "customer_name", "date", "owning_percentage"]
          }
        }
      },
      "required": ["unsuccessful", "active", "list"]
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
  }
}

