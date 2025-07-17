import React, { useState } from 'react';

const API_BASE_URL = 'http://localhost:8000';

const EmissionForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    material: '',
    quantity: '',
    unit: '',
    date_of_activity: '',
    location: ''
  });
  const [submitLoading, setSubmitLoading] = useState(false);

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  // const handleSubmit = async () => {
  //   // Basic validation
  //   if (!formData.material || !formData.quantity || !formData.unit || !formData.date_of_activity || !formData.location) {
  //     onSubmit('Please fill in all fields.');
  //     return;
  //   }

  //   setSubmitLoading(true);
    
  //   try {
  //     const response = await fetch(`${API_BASE_URL}/emission-records`, {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json',
  //       },
  //       body: JSON.stringify({
  //         ...formData,
  //         quantity: parseFloat(formData.quantity)
  //       })
  //     });

  //     if (response.ok) {
  //       onSubmit('Emission record submitted successfully!');
  //       setFormData({
  //         material: '',
  //         quantity: '',
  //         unit: '',
  //         date_of_activity: '',
  //         location: ''
  //       });
  //     } else {
  //       onSubmit('Error submitting record. Please try again.');
  //     }
  //   } catch (error) {
  //     onSubmit('Error submitting record. Please try again.');
  //   } finally {
  //     setSubmitLoading(false);
  //   }
  // };


  const handleSubmit = async () => {
  // Basic validation
  if (!formData.material || !formData.quantity || !formData.unit || !formData.date_of_activity || !formData.location) {
    onSubmit('Please fill in all fields.');
    return;
  }

  console.log("📦 Payload being submitted:", formData);

  try {
    const response = await fetch('http://127.0.0.1:8000/emission-records', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    });

    const result = await response.json();

    if (response.ok) {
      console.log("✅ Submission successful:", result);
      onSubmit(null, result); // success
    } else {
      console.error("❌ Backend error response:", result);
      onSubmit(result?.detail || 'Error submitting record. Please try again.');
    }
  } catch (error) {
    console.error("❌ Network or server error:", error);
    onSubmit('Network error: ' + error.message);
  }
};


  return (
    <div className="bg-white rounded-lg shadow-sm p-6">
      <h2 className="text-xl font-semibold text-gray-900 mb-4">Submit Emission Data</h2>
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Material</label>
          <input
            type="text"
            name="material"
            value={formData.material}
            onChange={handleInputChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="e.g., Diesel, Natural Gas, Electricity"
          />
        </div>
        
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Quantity</label>
            <input
              type="number"
              name="quantity"
              value={formData.quantity}
              onChange={handleInputChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="e.g., 100"
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Unit</label>
            <input
              type="text"
              name="unit"
              value={formData.unit}
              onChange={handleInputChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="e.g., liters, kWh"
            />
          </div>
        </div>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Date of Activity</label>
          <input
            type="date"
            name="date_of_activity"
            value={formData.date_of_activity}
            onChange={handleInputChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Location</label>
          <input
            type="text"
            name="location"
            value={formData.location}
            onChange={handleInputChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="e.g., Mumbai, India"
          />
        </div>
        
        <button
          onClick={handleSubmit}
          disabled={submitLoading}
          className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
        >
          {submitLoading ? 'Submitting...' : 'Submit Emission Record'}
        </button>
      </div>
    </div>
  );
};

export default EmissionForm;