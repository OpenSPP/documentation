// Custom version switcher for sphinx-book-theme 0.3.3
document.addEventListener('DOMContentLoaded', function() {
    // Fetch the switcher.json
    fetch('/_static/switcher.json')
        .then(response => response.json())
        .then(versions => {
            // Create switcher HTML
            const switcherHtml = `
                <div class="version-switcher" style="padding: 0.5em;">
                    <select id="version-select" style="padding: 0.25em; border-radius: 4px;">
                        ${versions.map(v => 
                            `<option value="${v.url}" ${v.version === getCurrentVersion() ? 'selected' : ''}>
                                ${v.name}
                            </option>`
                        ).join('')}
                    </select>
                </div>
            `;
            
            // Insert into navbar
            const navbar = document.querySelector('.openspporglink');
            if (navbar && navbar.parentElement) {
                navbar.parentElement.insertAdjacentHTML('afterbegin', switcherHtml);
                
                // Handle version change
                document.getElementById('version-select').addEventListener('change', function(e) {
                    const newUrl = e.target.value;
                    // Get current page path, removing any version prefix
                    let currentPath = window.location.pathname;
                    
                    // Remove version prefixes: /previews/branch-name/ or /version/
                    // This regex matches /previews/anything/ at the start
                    currentPath = currentPath.replace(/^\/previews\/[^\/]+\//, '/');
                    // This regex matches /version-number/ patterns at the start
                    currentPath = currentPath.replace(/^\/[0-9.]+\//, '/');
                    // Remove leading slash since newUrl already has trailing slash
                    currentPath = currentPath.replace(/^\/+/, '');
                    
                    // Navigate to same page in new version
                    window.location.href = newUrl + currentPath;
                });
            }
        })
        .catch(err => console.log('Version switcher not available:', err));
});

function getCurrentVersion() {
    // Extract version from URL or page title
    const title = document.querySelector('title');
    if (title && title.textContent.includes(' v')) {
        return title.textContent.split(' v')[1].split(' ')[0];
    }
    return 'stable';
}