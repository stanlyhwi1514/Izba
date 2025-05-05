playbook_template_schema = {
  "title": "Playbook",
  "type": "object",
  "required": [
    "customer_id"
    "playbook_type",
    "name",
    "description",
    "date",
    "associated_roles",
    "associated_skills",
    "workflow",
    "created_at",
    "updated_at"
  ],
  "properties": {
    "customer_id": { "type": "string" },
    "playbook_type": { "type": "string" },
    "name": { "type": "string" },
    "description": { "type": "string" },
    "date": {
      "type": "string",
      "pattern": "^(0[1-9]|[12][0-9]|3[01])/([0][1-9]|1[0-2])/([0-9]{4})$"  # DD/MM/YYYY format
    },
    "associated_roles": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1
    },
    "associated_skills": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1
    },
    "workflow": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["step_name", "description", "trigger_event", "finish_by_days", "owners"],
        "properties": {
          "step_name": { "type": "string" },           # E.g., "Detect Risk Signal"
          "description": { "type": "string" },         # Small detail about the step
          "trigger_event": { "type": "string" },        # E.g., "Post Risk Detection"
          "finish_by_days": { "type": "integer", "minimum": 0 },  # E.g., 3
          "owners": {
            "type": "array",
            "items": { "type": "string" },              # E.g., ["SME", "Executive"]
            "minItems": 1
          }
        }
      }
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "updated_at": {
      "type": "string",
      "format": "date-time"
    },
    "successful": {
        "type": "boolean"
    },
    "active": {
        "type": "boolean"
    }
  }
}
