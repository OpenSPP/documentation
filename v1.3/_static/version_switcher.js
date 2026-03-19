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
                    // Navigate to the landing page of the selected version
                    window.location.href = e.target.value;
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