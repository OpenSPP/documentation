// Review Status JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Try to extract from meta tags first
    let reviewStatus = document.querySelector('meta[name="review-status"]');
    let reviewDate = document.querySelector('meta[name="review-date"]');
    let reviewer = document.querySelector('meta[name="reviewer"]');
    
    let status = null;
    let date = null;
    let reviewerName = null;
    
    if (reviewStatus && reviewStatus.getAttribute('content') && 
        reviewStatus.getAttribute('content') !== 'review-status') {
        // Meta tags have actual values
        status = reviewStatus.getAttribute('content');
        date = reviewDate ? reviewDate.getAttribute('content') : null;
        reviewerName = reviewer ? reviewer.getAttribute('content') : null;
    } else {
        // Meta tags exist but have field names as content, so parse from source
        // Look for frontmatter in the raw HTML
        const pageSource = document.documentElement.innerHTML;
        
        // More robust regex patterns
        const statusMatch = pageSource.match(/review-status:\s*([^\n\r<]+)/);
        const dateMatch = pageSource.match(/review-date:\s*([^\n\r<]+)/);
        const reviewerMatch = pageSource.match(/reviewer:\s*([^\n\r<]+)/);
        
        if (statusMatch) {
            status = statusMatch[1].trim().replace(/['"]/g, '');
            if (dateMatch) date = dateMatch[1].trim().replace(/['"]/g, '');
            if (reviewerMatch) reviewerName = reviewerMatch[1].trim().replace(/['"]/g, '');
        }
    }
    
    if (status) {
        console.log('Review status detected:', status, 'Date:', date, 'Reviewer:', reviewerName);
        
        // Create and add ribbon
        createStatusRibbon(status);
        
        // Create and add banner if needed
        if (status !== 'approved') {
            createStatusBanner(status, date, reviewerName);
        }
    } else {
        console.log('No review status found');
        console.log('Meta tag content:', reviewStatus ? reviewStatus.getAttribute('content') : 'No meta tag');
    }
});

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
        const mainContent = document.querySelector('main') || document.querySelector('.bd-main');
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