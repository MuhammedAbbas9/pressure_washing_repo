window.addEventListener('load', async function () {
    const servicesContainer = document.getElementById('servicesContainer');
    console.log("servicesContainer value: " + servicesContainer);

    if (!servicesContainer) {
        console.error('Error: services-container element not found');
        return;
    }

    try {
        const response = await fetch('assets/data/services.json');
        if (!response.ok) throw new Error('Failed to load services.json');

        const services = await response.json();
        services.forEach(service => {
            const serviceItem = document.createElement('div');
            serviceItem.className = `col-lg-6`;
            serviceItem.setAttribute('data-aos', 'fade-up');
            serviceItem.setAttribute('data-aos-delay', service.delay);

            serviceItem.innerHTML = `
                <div class="service-item d-flex">
                    <div class="icon flex-shrink-0"><i class="${service.icon}"></i></div>
                    <div>
                        <h4 class="title"><a href="${service.link}" class="stretched-link">${service.title}</a></h4>
                    </div>
                </div>
            `;

            servicesContainer.appendChild(serviceItem);
        });
    }
    catch (error) {
        console.error('Error loading services:', error);
    }

});