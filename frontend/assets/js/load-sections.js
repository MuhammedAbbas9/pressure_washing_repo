document.addEventListener('DOMContentLoaded', () => {
    // Map of container IDs and corresponding section files
    const sections = {
        header: '../components/header.html',    // Load the "home.html" into header
        footer: '../components/footer.html',  // Load the "footer.html" into footer
        servicesList: '../sections/services-list.html'  // Load the "services-list.html" into services-list

    };

    // Function to load a section
    const loadSection = async (containerId, filePath) => {
        try {
            const response = await fetch(filePath);
            if (!response.ok) throw new Error(`Failed to load ${filePath}`);
            const content = await response.text();
            document.getElementById(containerId).innerHTML = content;
        } catch (error) {
            console.error(`Error loading section ${containerId} from ${filePath}:`, error);
        }
    };

    // Loop through sections and load each one
    for (const [id, file] of Object.entries(sections)) {
        loadSection(id, file);
    }
});