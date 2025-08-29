---
orphan: true
---

# G2P Profile Image

The G2P Profile Image module enables OpenSPP users to associate a single, distinct profile image with each registrant. This enhances visual identification and personalizes registrant profiles within the system.

## Purpose

This module streamlines the management of registrant profile pictures, providing a clear visual identifier for individuals and groups. It ensures that all profile images are appropriately sized and centrally stored, contributing to a more intuitive and efficient user experience for program administrators and case workers.

*   **Visual Identification:** Provides a clear profile picture for each registrant, aiding in quick visual recognition for case workers and administrators.
*   **Centralized Profile Management:** Allows users to easily upload, update, and manage a single profile image directly within the registrant's record.
*   **Automated Image Optimization:** Automatically resizes and compresses uploaded images to meet system requirements, ensuring efficient storage and fast loading times without user intervention.
*   **Data Integrity and Uniqueness:** Enforces a "one profile image per registrant" policy, preventing duplicate profile pictures and maintaining a clean, consistent record.
*   **Enhanced User Experience:** Personalizes registrant profiles, making them more engaging and easier to navigate for OpenSPP users.

## Dependencies and Integration

The G2P Profile Image module extends core OpenSPP functionalities by integrating seamlessly with the platform's foundational registry and document management systems.

This module builds upon the `res.partner` model, which is managed by the [G2P Registry Base](g2p_registry_base) module. It directly attaches profile images to these core registrant records, ensuring that every individual or group in the registry can have a designated profile picture.

It also integrates closely with the [G2P Registry Documents](g2p_registry_documents) module. Profile images are treated as a special type of document and are stored using the `storage.file` model provided by this module. This ensures that profile images benefit from the same secure storage backends and robust document management capabilities as other supporting documents.

## Additional Functionality

The G2P Profile Image module offers key features to manage and optimize registrant profile pictures effectively:

### Profile Image Upload and Replacement

Users can easily upload a profile image directly to a registrant's record. If a registrant already has a profile image, the system guides the user to replace the existing one, ensuring that only one active profile picture is maintained per registrant. This prevents accidental duplication and keeps the registrant's profile current.

### Automated Image Optimization

Upon upload, the module automatically processes images to ensure they meet system requirements. It resizes and compresses images larger than 1MB to optimize storage space and improve loading performance across the platform. This ensures high-quality visuals without burdening the system or requiring manual image preparation from users.

### Secure and Centralized Storage

All profile images are securely stored within OpenSPP's integrated document management system. They are associated with a specific "Profile Image" tag, making them easily identifiable and retrievable, while leveraging the system's robust backend for data security and scalability.

## Conclusion

The G2P Profile Image module is essential for enhancing visual identification and personalizing registrant profiles, contributing to a more efficient and user-friendly experience within OpenSPP.