import React, { useState } from 'react';

import '../css/dates.css';


export default function Home() {
  const [testData, setTestData] = useState(null);

  const handleTestBackend = async () => {
    try {
      const response = await fetch('https://dates-fd71bc03469b.herokuapp.com/test_data');
      const jsonData = await response.json();
      setTestData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  
  
  return (
    <div className="App">
      <div className='background-img'></div>
      <div className="line left-line"></div>
      <div className="line right-line"></div>
      <div id="header-hero">
        <section className="hero">
          <div className="hero-content">
            <h1>Discover a Culinary Journey</h1>
            <p>Experience the essence of Japanese cuisine at Wakuda</p>
            <a href="#header-hero" className="cta-button">
              Book a Table
            </a>
          </div>
        </section>
      </div>
      <section className="about-section">
        <div className="about-content">
            <h2>About Us</h2>
            <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et
            felis non velit ultrices consectetur sit amet ac urna. Vivamus vel
            quam tellus. Morbi bibendum ipsum a sem mattis vehicula. Vestibulum
            aliquet ex ut lorem feugiat, nec finibus risus mattis.
            </p>
            {/* Button to test backend */}
            <button onClick={handleTestBackend}>Test Backend</button>
            
            {/* Display fetched data */}
            {testData && (
              <div>
                <h2>Test Data</h2>
                <pre>{JSON.stringify(testData, null, 2)}</pre>
              </div>
            )}
        </div>
      </section>
      <footer className="footer">
        <p>&copy; 2024 Aaron Tran</p>
      </footer>
    </div>
  );
}
