import React from 'react';
import './App.scss';
import Header from './components/Header/Header';
import Categories from './components/Categories/Categories';
import Carousel from './components/Carousel/Carousel';

const App: React.FC = () => {
  return (
    <div className="App">
      <Header />
      <Carousel />
    </div>
  );
};

export default App;
