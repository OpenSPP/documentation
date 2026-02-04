/**
 * Enhance Sphinx search with fuzzy matching using Fuse.js
 * Falls back to fuzzy search when exact matches fail
 */

import Fuse from 'https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.mjs';

// Store original search function
const originalPerformSearch = Search.performSearch;

// Enhanced search with fuzzy fallback
Search.performSearch = function(query) {
    const results = originalPerformSearch.call(this, query);

    // If we have good results, return them
    if (results && results.length > 3) {
        return results;
    }

    // Try fuzzy matching on titles and terms
    const searchData = [];
    for (const [title, , , , score] of Search._index.titles) {
        searchData.push({ title, originalScore: score });
    }

    const fuse = new Fuse(searchData, {
        keys: ['title'],
        threshold: 0.4,  // 0 = exact, 1 = match anything
        includeScore: true,
        ignoreLocation: true
    });

    const fuzzyResults = fuse.search(query);

    // Merge exact and fuzzy results
    return [...results, ...fuzzyResults.map(r => r.item)];
};
