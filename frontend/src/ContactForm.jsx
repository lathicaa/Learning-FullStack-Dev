import {useState} from "react"

const ContactForm = ({ existingContact = {}, updateCallBack}) => {

    // need some state for our form, need to store the first name, last name, and email, then we are going to use that and submit it to the API to create a new contact
    const [firstName, setFirstName] = useState(existingContact.firstName || "")
    const [lastName, setLastName] = useState(existingContact.lastName || "")
    const [email, setEmail] = useState(existingContact.email || "")
    
    // if you passed us an object that has at least 1 entry inside of it, then we are updating it bc that means we have some existing data, if it doesn't it means we are creating a new contact
    const updating = Object.entries(existingContact).length !== 0

    // need a function so that when we press on the create contact button it actually makes that contact
    const onSubmit = async (e) => {
        e.preventDefault() // because we don't want to refresh the page automatically

        // going to set up a post request so that we can actually create the contact
        // need to define the data that we want to pass with out json as the requests, corresponds with what we are looking for in the api when we are creating a new contact
        // this is a javascript object, just like in python we need to convert it into a valid JSON object
        const data = {
            firstName,
            lastName,
            email
        }

        // defining the URL and endpoint
        const url = "http://127.0.0.1:5000/" + (updating ? `update_contact/${existingContact.id}` : "create_contact")
        // setting the options for the request
        const options = { 
            method: updating ? "PATCH" : "POST",
            headers: {
                // specifying that we are about to submit json data, need to include it in the header so that the API knows that we are going to submit json data
                "Content-Type": "application/json" 
            },
            // converts data to json string
            body: JSON.stringify(data) 
        }

        // sending the request 
        const response = await fetch(url, options)
        // checking for errors
        if (response.status !== 201 && response.status !== 200) { 
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallBack()
        }

    }


    return (
    <form onSubmit = {onSubmit} >
        <div>
            <label htmlFor = "firstName">First Name:</label>
            <input 
                type = "text" 
                id = "firstName" 
                value = {firstName} 
                onChange = {(e) => setFirstName(e.target.value)} 
            />
        </div>
        <div>
            <label htmlFor = "lastName">Last Name:</label>
            <input 
                type = "text" 
                id = "lastName" 
                value = {lastName} 
                onChange = {(e) => setLastName(e.target.value)} 
            />
        </div>
        <div>
            <label htmlFor = "email">Email:</label>
            <input 
                type = "text" 
                id = "email" 
                value = {email} 
                onChange = {(e) => setEmail(e.target.value)} 
            />
        </div> 
        <button type = "submit">{updating ? "Update" : "Create"} </button>           
    </form>

    );
}

export default ContactForm