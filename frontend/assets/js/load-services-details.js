document.addEventListener('DOMContentLoaded', async () => {
    const servicesContainer = document.getElementById('services-details');

    if (!servicesContainer) {
        console.error('Error: services-container element not found');
        return;
    }

    try {
        const response = await fetch('/wash_services');
        if (!response.ok) throw new Error('Failed to load services-details.json');

        const services = await response.json();
        services.forEach((service, index) => {
            console.log("service # " + index);
            if (index % 2 === 1) {
                const serviceItem = document.createElement('div');
                serviceItem.className = 'service reverse';

                serviceItem.innerHTML = `
                    <div class="service-image">
                        <img src="${service.images_path}" alt="${service.type}">
                    </div>
                    <div class="service-content">
                        <h2>${service.type}</h2>
                        <p>${service.description}</p>
                        <a href="starter-page.html">
                            <button class="choose-service">Choose this service</button>
                        </a>                    
                    </div>
                `;

                servicesContainer.appendChild(serviceItem);
            }
            else {

                const serviceItem = document.createElement('div');
                serviceItem.className = 'service';

                serviceItem.innerHTML = `
                    <div class="service-content">
                        <h2>${service.type}</h2>
                        <p>${service.description}</p>
                        <a href="starter-page.html">
                            <button class="choose-service">Choose this service</button>
                        </a>
                    </div>
                    <div class="service-image">
                        <img src="${service.images_path}" alt="${service.type}">
                    </div>
                `;

                servicesContainer.appendChild(serviceItem);

            }

        });
    } catch (error) {
        console.error('Error loading services:', error);
    }
});