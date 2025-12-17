---
openspp:
  doc_status: unverified
---

# Event data

Event data lets you record **time-based observations** about registrants (individuals or groups) without changing their core profile each time. Typical uses include surveys, field visits, assessments, and syncs from external data collection tools.

Unlike a single profile field, event data is **repeatable** (many events per registrant), has its own **lifecycle** (draft/active/superseded/expired), and can capture **source information** (who collected it, when, and from which system).

## Create an event type (Studio)

Event types define the fields you collect each time an event is recorded.

1. Go to **Studio → Event Types**.
2. Click **Create** (or use the wizard).
3. Configure:
   - **Event Type Name** (for example “Household Visit”)
   - **Target Type** (Individual, Group, or Both)
   - **Fields** (the questions/values you want to capture)
   - Optional:
     - **Allow Multiple Events** (if disabled, activating a new event supersedes the previous active one)
     - **Requires Approval** (new events start in “Pending Approval”)
     - **Programs** (limit visibility to specific programs)
4. Click **Activate**.

Notes:
- After activation, Studio creates a corresponding **Event Type** record under the hood. You can open it from the Studio form using **View Event Type**.
- Screenshot placeholders:
  - `event_data/studio_event_types_list.png`
  - `event_data/studio_event_type_form.png`
  - `event_data/studio_event_type_fields.png`

## Record event data

You can create an event record either from a registrant record or directly from Studio.

### Option A — From a registrant (quick entry)

1. Open an Individual or Group registrant.
2. Click the **Event Data** button in the header (stat button).
3. Select the **Event Type**, set **Collection Date**, and (optionally) **Collector Name**.
4. Click **Create Event**.

If the event type uses a dedicated data model, the wizard redirects you to the corresponding data entry screen. Otherwise, the event values are stored in the event’s JSON payload and rendered in the **Event Data** tab of the event record.

Screenshot placeholders:
- `event_data/registrant_event_data_button.png`
- `event_data/create_event_wizard.png`
- `event_data/event_record_form.png`

### Option B — From Studio (guided field entry)

1. Go to **Studio → Event Types** and open an active event type.
2. Click **Enter Event**.
3. Select the registrant, fill in values, and click **Create Event**.

Screenshot placeholders:
- `event_data/enter_event_wizard.png`

## Event lifecycle (draft → active → superseded/expired)

Event records support states such as:

- **Draft**: captured but not yet applied/considered current
- **Active**: considered the current event (for event types that keep one active event per registrant)
- **Superseded**: replaced by a newer event
- **Expired**: automatically expired based on configured rules

Key behaviors:

- If an event type is configured to keep only one active event per registrant, activating a new event supersedes the previous active event.
- Event types can automatically set an expiry date (for example “expire after N days”). A scheduled job updates active events to **Expired** when needed.

## Using event data in variables and expressions (advanced)

Event data is designed to be usable in downstream logic (for example eligibility rules, dashboards, scoring, and validation) through **variables** and **expressions**.

In deployments that include the event/CEL integration, you can create variables that aggregate over events, such as:

- Number of “Household Visit” events within the last 90 days
- Maximum “assessment_score” seen in events this year

This is configured in **Studio → Variables** by using an **Aggregate** variable targeting **Events**.

For the CEL syntax and available helper functions (`event`, `has_event`, `events_count`, …), see {doc}`../technical_reference/cel/events`.
