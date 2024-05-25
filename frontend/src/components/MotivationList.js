import React from 'react';

const MotivationList = ({ sentences }) => {
  return (
    <div>
      <h2>Motivation Sentences</h2>
      <ul>
        {sentences.map((sentence, index) => (
          <li key={index}>{sentence}</li>
        ))}
      </ul>
    </div>
  );
};

export default MotivationList;