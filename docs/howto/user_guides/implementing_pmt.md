# PMT via the UI

This guide elucidates the steps required to implement Proxy Means Testing (PMT) within the OpenSPP system, leveraging Odoo's user interface customization features. By following through, one will learn how to add custom fields to models and modify views to accommodate the newly introduced data fields to implement PMT.

1. Activation of Developer Mode

   - Ensure administrative access is granted.
   - Navigate to the Settings module.
   - Scroll towards the bottom and select "Activate the developer mode".

2. Model Customization

   - With the objective of adding fields to the `res.partner` model, proceed to Settings -> Technical -> Models (located under Database Structure) and choose the `res.partner` model.
   - Fields such as x_education_level and x_household_size are to be added.
   - Upon pressing `Add a line`, a properties panel unveils, facilitating the specification of Field Name, Field Label, Field Type, among other attributes.
   - Choose the field type (e.g., Integer, Selection, Float) from the left-hand panel and fill the Field Name(x_education_level, x_household_size) ,and the Field Label.
   - Following the addition of each field, select “Save and Close”.
   - An additional computed field named x_pmt_score is to be introduced. Adhere to the preceding steps, with the added configurations outlined below:
     - Dependencies: x_education_level, x_household_size
     - Function:
       for record in self:
       record['x_pmt_score'] = record['x_education_level'] \* record['x_household_size']
   - Click "Save" situated on the top right to retain the modifications.

3. View Modification

   - Aiming to integrate fields into the individual view, opt for `view_individuals_form` view. Navigate via Settings -> Technical -> View (found under User Interface) and select the view.
   - Edit the view, incorporating the following:

   ```xml
   <page name="PMT" string="Proxy Means Testing">
       <group col="4" colspan="4">
           <field name="x_education_level"/>
           <field name="x_household_size"/>
           <field name="x_pmt_score" readonly="1"/>
       </group>
   </page>
   ```

   - Select "Save" on the top right to preserve the alterations.

4. Access Registry

   - Click on the "Registry" menu item situated at the screen’s top.
   - Choose "Individuals".
   - Pick a record to view the aforementioned changes.
   - Now the PMT score will be calculated according to the given function defined above.

Upon completion, a new tab titled "Proxy Means Testing" should now be present within the Registry in the individual’s record as a new tab.
