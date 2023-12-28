function getBirdRecommendations(birdType) {
    switch (birdType) {
        case "Pigeons":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing, Bird spikes
            Medium Recommendation: Distress and Alarm calls, Reflectors
            Limited Recommendation: Laser, Rc Model Drone
            Not Recommended: Ultrasound, Chemical
            Distress and Alarm calls: 1
            `;

        case "Doves":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing, Bird spikes
            Medium Recommendation: Distress and Alarm calls, Reflectors
            Limited Recommendation: Laser, Rc Model Drone
            Not Recommended: Ultrasound, Chemical
            Distress and Alarm calls: 1
            `;

        case "Crows":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing
            Medium Recommendation: Distress and Alarm calls, Reflectors (Limited references)
            Limited Recommendation: Laser
            Not Recommended: Ultrasound, Chemical, Rc Model Drone
            Distress and Alarm calls: 2
            `;

        case "Blackbirds":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing
            Medium Recommendation: Distress and Alarm calls, Reflectors
            Limited Recommendation: Laser
            Not Recommended: Ultrasound, Chemical, Rc Model Drone
            Distress and Alarm calls: 3
            `;

        case "Cowbirds":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing
            Medium Recommendation: Distress and Alarm calls, Reflectors
            Limited Recommendation: Laser
            Not Recommended: Ultrasound, Chemical, Rc Model Drone
            Distress and Alarm calls: 3
            `;

        case "European Starlings":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing
            Medium Recommendation: Distress and Alarm calls, Reflectors
            Limited Recommendation: Laser
            Not Recommended: Ultrasound, Chemical, Rc Model Drone
            Distress and Alarm calls: 3
            `;

        case "Sparrows":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing
            Medium Recommendation: Distress and Alarm calls, Reflectors
            Limited Recommendation: Laser
            Not Recommended: Ultrasound, Chemical, Rc Model Drone
            Distress and Alarm calls: 3
            `;

        case "Cormorants":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing
            Medium Recommendation: Distress and Alarm calls, Reflectors
            Limited Recommendation: Laser
            Not Recommended: Ultrasound, Chemical, Rc Model Drone
            Distress and Alarm calls: 3
            `;

        case "Waterfowls":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing
            Medium Recommendation: Distress and Alarm calls, Reflectors
            Limited Recommendation: Laser
            Not Recommended: Ultrasound, Chemical, Rc Model Drone
            Distress and Alarm calls: 3
            `;

        case "Mallards":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing
            Medium Recommendation: Distress and Alarm calls, Reflectors
            Limited Recommendation: Laser
            Not Recommended: Ultrasound, Chemical, Rc Model Drone
            Distress and Alarm calls: 3
            `;

        case "Owls":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing
            Medium Recommendation: Distress and Alarm calls, Reflectors
            Limited Recommendation: Laser
            Not Recommended: Ultrasound, Chemical, Rc Model Drone
            Distress and Alarm calls: 3
            `;

        case "Geese":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing
            Medium Recommendation: Distress and Alarm calls, Reflectors
            Limited Recommendation: Laser
            Not Recommended: Ultrasound, Chemical, Rc Model Drone
            Distress and Alarm calls: 3
            `;

        case "Gulls":
            return `
            Types of Bird: ${birdType}
            Highly Recommended: Netting and fencing, Aircraft Hazing
            Medium Recommendation: Reflectors
            Limited Recommendation: Laser, Distress and Alarm calls
            Not Recommended: Ultrasound, Chemical, Rc Model Drone, Magnet Devices
            Distress and Alarm calls: Not Recommended
            `;

        default:
            return "Bird type not recognized.";
    }
}

// Example usage
console.log(getBirdRecommendations("Pigeons"));
