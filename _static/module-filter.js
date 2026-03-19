/**
 * Product/Module filter widget for OpenSPP documentation
 * Filters navigation items based on user's selected modules
 */

class ModuleFilter {
    constructor() {
        this.metadata = null;
        this.selectedModules = this.loadPreferences();
        this.init();
    }

    async init() {
        // Load metadata
        try {
            const response = await fetch('/_static/product-metadata.json');
            this.metadata = await response.json();
        } catch (error) {
            console.error('Failed to load product metadata:', error);
            return;
        }

        // Render filter widget
        this.renderWidget();

        // Apply initial filter
        this.applyFilter();
    }

    loadPreferences() {
        const saved = localStorage.getItem('openspp-selected-modules');
        if (saved) {
            return JSON.parse(saved);
        }
        // Default: show all modules
        return null;  // null = show all
    }

    savePreferences() {
        localStorage.setItem('openspp-selected-modules', JSON.stringify(this.selectedModules));
    }

    renderWidget() {
        // Only render on search page
        const searchPageFilter = document.getElementById('search-module-filter-options');

        if (searchPageFilter) {
            // Render checkboxes inline on search page
            this.renderSearchPageFilter(searchPageFilter);
        }
    }

    renderSearchPageFilter(container) {
        // Add checkboxes for each product inline
        this.metadata.all_products.filter(p => p !== 'core').forEach(product => {
            const wrapper = document.createElement('div');
            wrapper.className = 'form-check form-check-inline';

            const checkbox = document.createElement('input');
            checkbox.className = 'form-check-input';
            checkbox.type = 'checkbox';
            checkbox.id = `search-module-${product}`;
            checkbox.value = product;
            checkbox.checked = !this.selectedModules || this.selectedModules.includes(product);

            const label = document.createElement('label');
            label.className = 'form-check-label';
            label.htmlFor = checkbox.id;
            label.textContent = this.formatProductName(product);

            wrapper.appendChild(checkbox);
            wrapper.appendChild(label);
            container.appendChild(wrapper);

            checkbox.addEventListener('change', () => this.onFilterChange());
        });
    }


    formatProductName(product) {
        const names = {
            'registry': 'Registry',
            'programs': 'Programs',
            'drims': 'DRIMS',
            'payments': 'Payments',
            'grievances': 'Grievances',
            'farmer_registry': 'Farmer Registry'
        };
        return names[product] || product;
    }

    onFilterChange() {
        // Query checkboxes from search page
        const checkboxes = document.querySelectorAll('#search-module-filter-options input[type="checkbox"]');

        const checked = Array.from(checkboxes)
            .filter(cb => cb.checked)
            .map(cb => cb.value);

        // If all checked, treat as "show all"
        if (checked.length === checkboxes.length) {
            this.selectedModules = null;
        } else {
            this.selectedModules = checked;
        }

        this.savePreferences();
        this.applyFilter();
    }

    applyFilter() {
        // Show all if no filter selected
        if (!this.selectedModules) {
            document.querySelectorAll('[data-openspp-products]').forEach(el => {
                el.classList.remove('module-filtered');
            });
            // Also remove filtering from list items
            document.querySelectorAll('li.module-filtered').forEach(el => {
                el.classList.remove('module-filtered');
            });
            return;
        }

        // Filter navigation items
        const navLinks = document.querySelectorAll('.bd-sidebar a.reference');

        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (!href) return;

            // Extract docname from href
            const docname = href.replace(/^\//, '').replace(/\.html.*$/, '');
            const docMeta = this.metadata.documents[docname];

            if (!docMeta) return;

            const docProducts = docMeta.products || [];

            // Show if: core docs OR any selected module matches
            const shouldShow = docProducts.includes('core') ||
                               docProducts.some(p => this.selectedModules.includes(p));

            const listItem = link.closest('li');
            if (listItem) {
                if (shouldShow) {
                    listItem.classList.remove('module-filtered');
                } else {
                    listItem.classList.add('module-filtered');
                }
            }
        });
    }
}

// Initialize when DOM ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => new ModuleFilter());
} else {
    new ModuleFilter();
}
