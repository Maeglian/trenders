import React from 'react';
import ReactDOM from 'react-dom';
import './Carousel.scss';

interface CarouselProps {
    title: string;
    list: string[];
}

class Carousel extends React.Component<CarouselProps> {
    public static defaultProps = {
        title: '',
        list: ['Что посмотреть', 'Фильмы', 'Сериалы', 'Мультфильмы', 'Блогеры', 'Спорт', 'Музыка', 'Игры'],
    };
    public render() {
        return (
            <div className="Carousel">
                <div className="Carousel-Header">
                    <div className="Carousel-HeaderTitle">{this.props.title}</div>
                    <div className="Carousel-HeaderHide"></div>
                </div>
                <div className="Carousel-List">
                    {this.props.list.map((item, num) =>
                        <div className="Carousel-ListItem" key={num}>{item}</div>)}
                </div>
            </div>
        );
    }
}

export default Carousel;
