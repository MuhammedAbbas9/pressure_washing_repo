document.addEventListener('DOMContentLoaded', async () => {
    // Map of container IDs and corresponding section files
    const sections = {
        servicesList: '../sections/services-list.html',  // Load the "services-list.html" into services-list
        header: '../components/header.html',    // Load the "home.html" into header
        footer: '../components/footer.html', // Load the "footer.html" into footer
        portfolioSec: '../pages/portfolio-details.html', // Load the "portfolio-details.html" into portfolioSec
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