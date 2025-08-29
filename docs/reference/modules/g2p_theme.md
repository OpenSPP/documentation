---
orphan: true
---

# G2P Theme

The `g2p_theme` module customizes the visual identity and user experience of the OpenSPP platform, particularly for user authentication and public-facing elements. It establishes a consistent brand presence and enhances security for specific user types within social protection programs.

## Purpose

This module provides a tailored and secure user interface experience for OpenSPP deployments. It ensures a professional and branded environment while implementing crucial access controls.

*   **Branded User Experience:** Delivers a consistent and professional visual identity across the platform, including login and password reset pages, enhancing trust and recognition for beneficiaries and administrators.
*   **Custom Login and Registration Flows:** Replaces standard authentication pages with OpenG2P-specific designs, streamlining the user journey for program participants and staff.
*   **Enhanced Security for Registrants:** Implements a critical security measure by preventing direct backend access for users designated as registrants, ensuring they interact only through designated frontend portals.
*   **Streamlined Password Management:** Provides a robust and user-friendly process for password resets, including clear validation to guide users effectively.
*   **Consistent Platform Branding:** Enables the configuration of a custom favicon, ensuring that the OpenSPP instance reflects the program's or organization's branding across all browser tabs.

## Dependencies and Integration

The `g2p_theme` module integrates closely with core OpenSPP functionalities to deliver its custom features. It builds upon existing frameworks to modify the user interface and authentication processes.

This module depends on the foundational [Base](base) module for core system functionalities and the [Web](web) module for the underlying user interface framework. It extends the [Auth Signup](auth_signup) module to provide custom registration and login page templates, and leverages the [Website](website) module for rendering these public-facing pages. By integrating with these modules, `g2p_theme` ensures that its custom branding and security enhancements are seamlessly applied to the standard OpenSPP authentication and user interface.

## Additional Functionality

### Custom User Interface and Branding

This module transforms the default OpenSPP interface into a branded experience tailored for social protection programs.

*   **Branded Authentication Pages:** Users encounter custom-designed login and password reset pages that reflect the OpenG2P visual identity. This creates a cohesive and trustworthy entry point for all users, from program staff to beneficiaries.
*   **System-Wide Favicon:** Organizations can configure a custom favicon, which appears in browser tabs and bookmarks, to maintain a consistent brand presence across the entire OpenSPP application. This small detail reinforces the professional image of the platform.
*   **Dynamic Window Titles:** The module dynamically adjusts the browser window title, providing more informative context to users as they navigate different sections of the OpenSPP backend.

### Enhanced User Access Control

The module introduces specific security measures to manage user access, particularly for beneficiaries or program participants.

*   **Registrant Login Restriction:** A crucial security feature prevents users designated as "registrants" (e.g., beneficiaries or farmers) from logging directly into the administrative backend of OpenSPP. This ensures that registrants can only access the system through intended public or self-service portals, protecting sensitive program data.
*   **Secure Password Reset Process:** The module refines the password reset workflow, ensuring that users can only reset their password if their login or email address uniquely identifies a single user in the system. This validation prevents ambiguity and enhances the security of the password recovery process.

## Conclusion

The `g2p_theme` module is essential for delivering a branded, secure, and user-friendly experience within OpenSPP, ensuring both visual consistency and robust access control for social protection programs.