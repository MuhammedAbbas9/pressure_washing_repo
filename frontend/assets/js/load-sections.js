document.addEventListener('DOMContentLoaded', async () => {
    // Map of container IDs and corresponding section files
    const sections = {
        header: '../components/header.html',    // Load the "home.html" into header
        hero: '../sections/hero.html',  // Load the "hero.html" into hero
        about: '../sections/about.html',  // Load the "about.html" into about
        stats: '../sections/stats.html',  // Load the "stats.html" into stats
        servicesList: '../sections/services-list.html',  // Load the "services-list.html" into services-list
        features: '../sections/features.html',  // Load the "features.html" into features
        footer: '../components/footer.html', // Load the "footer.html" into footer
        portfolio: '../sections/portfolio.html', // Load the "portfolio.html" into portfolio
        callToAction: '../sections/call-to-action.html', // Load the "call-to-action.html" into call-to-action
        breadcrumb1: '../components/breadcrumb.html', // Load the "breadcrumb.html" into breadcrumb
    };

    // Function to load a section
    const loadSection = async (containerId, filePath) => {
        try {
            console.log(`Loading section ${containerId} from ${filePath}`);
            const response = await fetch(filePath);
            if (!response.ok) throw new Error(`Failed to load ${filePath}`);
            const content = await response.text();
            console.log("content: " + content);
            document.getElementById(containerId).innerHTML = content;
        } catch (error) {
            console.error(`Error loading section ${containerId} from ${filePath}:`, error);
        }
    };

    // Loop through sections and load each one
    for (const [id, file] of Object.entries(sections)) {
        console.log(`Loading section ${id} from ${file}`);
        loadSection(id, file);
    }
});