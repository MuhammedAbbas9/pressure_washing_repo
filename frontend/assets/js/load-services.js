window.addEventListener('load', async function () {
    const servicesContainer = document.getElementById('servicesContainer');
    console.log("servicesContainer value: " + servicesContainer);

    if (!servicesContainer) {
        console.error('Error: services-container element not found');
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/wash_services');
        if (!response.ok) throw new Error('Failed to load services.json');

        const services = await response.json();
        services.forEach(service => {
            const serviceItem = document.createElement('div');
            serviceItem.className = `col-lg-6`;
            serviceItem.setAttribute('data-aos', 'fade-up');
            let delay = 100;
            serviceItem.setAttribute('data-aos-delay', delay);
            delay += 100;

            serviceItem.innerHTML = `
                <div class="service-item d-flex">
                    <div class="icon flex-shrink-0"><i class="${service.images_path}"></i></div>
                    <div>
                        <h4 class="title"><a href="" class="stretched-link">${service.type}</a></h4>
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