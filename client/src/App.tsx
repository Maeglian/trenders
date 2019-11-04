import React from 'react';
import {Provider} from 'react-redux';
import './App.scss';
import Header from './components/Header/Header';
import Categories from './components/Categories/Categories';
import Trends from './components/Trends/Trends';
import store from './store/createStore';

const App: React.FC = () => {
  return (
    <Provider store={store}>
      <div className="App">
        <Header />
        <Categories />
        <div className="App-Content">
          <Trends />
        </div>
      </div>
    </Provider>
  );
};

export default App;
