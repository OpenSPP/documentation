// Simplified Review Status System
// Since MyST/Sphinx strips frontmatter from HTML output, we'll use a simpler approach

document.addEventListener('DOMContentLoaded', function() {
    console.log('Review status system loading...');
    
    // For now, determine status based on URL patterns
    const currentPath = window.location.pathname;
    console.log('Current path:', currentPath);
    
    let status = determineStatusFromPath(currentPath);
    console.log('Determined status:', status);
    
    if (status) {
        console.log('Creating ribbon and banner for status:', status);
        
        // Create and add ribbon
        createStatusRibbon(status);
        
        // Create and add banner if needed
        if (status !== 'approved') {
            createStatusBanner(status, getCurrentDate(), 'migration-script');
        }
        
        console.log('Review status system active');
    } else {
        console.log('No status determined for path:', currentPath);
    }
});

function determineStatusFromPath(path) {
    // Pattern-based status assignment based on the reorganization
    
    // Approved: newly created files
    if (path.includes('/installation_pypi.html') ||
        path.includes('/case_studies/index.html') ||
        path.includes('/features/index.html') ||
        path.includes('/customization/index.html') ||
        path.includes('/integrations/index.html') ||
        path.includes('/api_usage/index.html') ||
        path.includes('/reference/api/index.html') ||
        path.includes('/reference/technical/index.html') ||
        path.includes('/registry_management/index.html') ||
        path.includes('/program_management/index.html') ||
        path.includes('/administration/index.html')) {
        return 'approved';
    }
    
    // Reviewed: simple moves
    if (path.includes('/community/') ||
        path.includes('/reference/modules/') ||
        path.includes('/reference/glossary.html') ||
        path.includes('/installation_docker.html') ||
        path.includes('/poc_and_pilot.html')) {
        return 'reviewed';
    }
    
    // Needs Review: everything else (complex restructures)
    if (path.includes('/user_guide/') ||
        path.includes('/overview/concepts/') ||
        path.includes('/developer_guide/customization/') ||
        path.includes('/developer_guide/integrations/') ||
        path.includes('/reference/technical/')) {
        return 'needs-review';
    }
    
    // Default for other pages
    return 'needs-review';
}

function getCurrentDate() {
    return new Date().toISOString().split('T')[0]; // YYYY-MM-DD format
}

function createStatusRibbon(status) {
    const ribbon = document.createElement('div');
    ribbon.className = `review-status-ribbon status-${status}`;
    
    const statusTexts = {
        'needs-review': 'Needs Review',
        'in-review': 'In Review',
        'reviewed': 'Reviewed',
        'approved': 'Approved',
        'outdated': 'Outdated'
    };
    
    ribbon.textContent = statusTexts[status] || 'Unknown';
    document.body.appendChild(ribbon);
}

function createStatusBanner(status, date, reviewer) {
    const banner = document.createElement('div');
    banner.className = `review-status-banner status-${status}`;
    
    const statusInfo = {
        'needs-review': {
            icon: '⚠️',
            text: 'This page needs review after the recent documentation reorganization.',
            action: 'Content may be outdated or moved from its original location.'
        },
        'in-review': {
            icon: '🔍',
            text: 'This page is currently being reviewed.',
            action: reviewer ? `Being reviewed by ${reviewer}` : 'Review in progress'
        },
        'reviewed': {
            icon: '✅',
            text: 'This page has been reviewed and updated.',
            action: date ? `Last reviewed: ${date}` : 'Recently reviewed'
        },
        'outdated': {
            icon: '📝',
            text: 'This page may contain outdated information.',
            action: 'Please check for more recent documentation or updates.'
        }
    };
    
    const info = statusInfo[status];
    if (info) {
        banner.innerHTML = `
            <div>
                <span class="status-icon">${info.icon}</span>
                <strong>${info.text}</strong>
            </div>
            <div class="status-details">${info.action}</div>
        `;
        
        // Insert banner at the top of the main content
        const mainContent = document.querySelector('main') || document.querySelector('.bd-main') || document.querySelector('#main-content');
        if (mainContent) {
            const firstChild = mainContent.firstElementChild;
            if (firstChild) {
                mainContent.insertBefore(banner, firstChild);
            } else {
                mainContent.appendChild(banner);
            }
        }
    }
}