import { useState, useEffect } from 'react';
import ContactList from "./ContactList";
import './App.css';
import ContactForm from "./ContactForm";

function App() {

  // stores our contacts, useState is an empty list that stores them
  const [contacts, setContacts] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentContact, setCurrentContact] = useState([])

  // as soon as this component loads, call the function, then fetchContacts will give us the contacts, then it sets it in the state, then we use it to list all the contacts out
  useEffect(() => {
    fetchContacts()
  }, []);

  // asynchronous function that will send a request to the backend to get the contact
  const fetchContacts = async () => {
    
    // fetch by defualt will send a get request to backend, sending get request to /contacts endpoint
    // waiting for this to give us a response, while we are waiting, want to get JSON data associated with response
    const response = await fetch("http://127.0.0.1:5000/contacts");
    const data = await response.json();
    console.log(data.contacts);
    setContacts(data.contacts);
  }

  const closeModal = () => {
    setIsModalOpen(false)
    setCurrentContact({})
  }

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  const openEditModal = (contact) => {
    if (isModalOpen) return
    setCurrentContact(contact)
    setIsModalOpen(true)
  }

  const onUpdate = () => {
    closeModal()
    fetchContacts()
  }

  return (
    <>
      <ContactList contacts = {contacts} updateContact={openEditModal} updateCallBack={onUpdate}/>
      <button onClick={openCreateModal}>Create New Contact</button>
      { isModalOpen && <div className = "modal">
        <div className="modal-content">
          <span className="close" onClick={closeModal}>&times;</span>
          <ContactForm existingContact={currentContact} updateCallBack={onUpdate}/>
        </div>
      </div>
      }
    </>
  );
}



export default App
