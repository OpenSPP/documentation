# G2P Program Autoenrol

The G2P Program Autoenrol module automates the enrollment of new registrants into eligible social protection programs, streamlining the process and reducing manual intervention.

## Purpose

This module enhances program management by automatically evaluating and enrolling new registrants based on predefined criteria. It significantly reduces administrative overhead and ensures that eligible individuals are promptly included in relevant programs.

*   **Automate Registrant Enrollment**: Automatically evaluates newly created registrants against program eligibility criteria for immediate enrollment. This ensures timely inclusion of beneficiaries without manual data entry.
*   **Define Dynamic Eligibility**: Allows program administrators to configure specific, data-driven rules (domains) for automatic enrollment. For example, a program might auto-enroll all new registrants from "Province A" aged "0-5 years".
*   **Manage Conditional Memberships**: Provides an option to automatically remove registrants from a program if they were auto-enrolled but subsequently fail more rigorous, full eligibility checks. This maintains data accuracy and program integrity.
*   **Maintain Real-time Program Counts**: Ensures that beneficiary counts for programs are updated immediately upon auto-enrollment or removal. This provides administrators with accurate, up-to-date program statistics.

## Dependencies and Integration

This module extends the core functionality of program management within OpenSPP.

The `g2p_program_autoenrol` module primarily depends on the [G2P Programs](g2p_programs) module. It integrates by adding new auto-enrollment fields and logic directly to existing program definitions, allowing administrators to configure auto-enrollment settings for each social protection program. When new registrants are created in the system (managed by `res.partner`), this module automatically triggers an evaluation against active programs configured for auto-enrollment. If a registrant meets the specified criteria, a program membership is automatically created and processed, leveraging the membership management features of the G2P ecosystem.

## Additional Functionality

### Automated Registrant Enrollment

This feature ensures that new registrants are automatically considered for active programs with auto-enrollment enabled. Upon a registrant's creation, the system evaluates their data against all relevant program criteria, enrolling them instantly if they qualify. This eliminates the need for manual review and enrollment for initial program entry.

### Configurable Eligibility Domains

Program administrators can define specific, dynamic eligibility rules for auto-enrollment using a powerful domain builder. This allows for highly granular targeting, such as enrolling all new registrants who are "female, under 18, and reside in District X." These domains ensure that only genuinely eligible registrants are automatically enrolled, based on their profile data.

### Conditional Membership Management

For programs requiring further validation beyond initial auto-enrollment criteria, this module offers a crucial safeguard. If a registrant is auto-enrolled but later fails a more comprehensive eligibility check during the enrollment process, the system can be configured to automatically remove that registrant's membership. This maintains the integrity of program beneficiary lists and prevents ineligible individuals from receiving benefits.

## Conclusion

The G2P Program Autoenrol module significantly streamlines beneficiary management by automating the initial enrollment of eligible registrants, ensuring efficiency and accuracy in social protection programs.