import React, { Component } from 'react';
import Carousel from '../Carousel/Carousel';
import './Categories.scss';


const categories = ['Что посмотреть', 'Фильмы', 'Сериалы', 'Мультфильмы', 'Блогеры', 'Спорт', 'Музыка', 'Игры'];

class Categories extends Component {
    public render() {
        return (
            <div className="Categories">
                <Carousel>
                {
                    categories.map((item, index) => (
                        <div className={`Categories-Item ${index === 0 && 'Categories-Item_state_active'}`}>
                            {item}
                        </div>
                    ))
                }
                </Carousel>
                
            </div>
        );
    }
}

export default Categories;
