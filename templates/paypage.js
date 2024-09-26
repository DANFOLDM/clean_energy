function confirmOrder() {
    const buyerName = document.getElementById('buyer-name').value;
    const buyerEmail = document.getElementById('buyer-email').value;
    const pickupPoint = document.getElementById('pickup-point').value;
    const paymentMethod = document.querySelector('input[name="payment"]:checked').value;

    if (buyerName && buyerEmail && pickupPoint && paymentMethod) {
        alert(`Order confirmed!\nName: ${buyerName}\nEmail: ${buyerEmail}\nPickup Point: ${pickupPoint}\nPayment Method: ${paymentMethod}`);
    } else {
        alert('Please fill in all required fields.');
    }
}

// Function to open the age verification modal
function openModal() {
    document.getElementById('ageVerificationModal').style.display = 'flex';
}

// Function to close the modal
function closeModal() {
    document.getElementById('ageVerificationModal').style.display = 'none';
}

// Function to simulate redirection to Privado.id for manual registration
function redirectToPrivado() {
    window.location.href = 'https://share-eu1.hsforms.com/1i-5lwzTvSuS4bxTaDfKX_Q2e55yy';
}

// Function to check if the user is registered with Privado.id
async function checkIfUserIsRegisteredWithPrivado(userId) {
    // Simulate checking with Privado API (You should replace this with a real check)
    return false; // Assuming the user is not registered for demo purposes
}

// Confirm order function
async function confirmOrder() {
    const phoneNumber = document.getElementById('phone_number').value;
    const userId = "exampleUserId"; // Replace with actual user's ID

    // Disable the button while processing
    document.getElementById('confirm_button').disabled = true;
    document.getElementById('message').innerHTML = 'Processing...';

    try {
        // Check if user is registered with Privado.id
        const isRegisteredWithPrivado = await checkIfUserIsRegisteredWithPrivado(userId);

        if (!isRegisteredWithPrivado) {
            openModal(); // If not registered, show the modal
            document.getElementById('message').innerHTML = ''; // Clear message
            return;
        }

        // User is registered, continue with order confirmation
        const response = await fetch('/confirm_order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_id: userId,
                phone_number: phoneNumber
            })
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById('message').innerHTML = result.message;
        } else {
            document.getElementById('message').innerHTML = result.error;
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('message').innerHTML = 'An error occurred. Please try again.';
    } finally {
        // Re-enable the button after processing
        document.getElementById('confirm_button').disabled = false;
    }
}
