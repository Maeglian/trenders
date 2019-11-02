import React, { Component } from 'react';
import './Categories.scss';


const categories = ['Что посмотреть', 'Блогеры', 'Фильмы', 'Сериалы'];

class Categories extends Component {
    public render() {
        return (
            <div className="Categories">
                {
                    categories.map((item, index) => (
                        <div className={`Categories-Item ${index === 0 && 'Categories-Item_state_active'}`}>
                            {item}
                        </div>
                    ))
                }
            </div>
        );
    }
}

export default Categories;
