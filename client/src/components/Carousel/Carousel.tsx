import React from 'react';
import ReactDOM from 'react-dom';
import './Carousel.scss';

interface CarouselProps {
    title: string;
    list: string[];
}

class Carousel extends React.Component<CarouselProps> {
    public render() {
        return (
            <div className="Carousel">
                <div className="Carousel-Header">
                    <div className="Carousel-HeaderTitle">{this.props.title}</div>
                    <div className="Carousel-HeaderHide"></div>
                </div>
                <ul className="Carousel-List">
                    {this.props.list.map((item, num) => {
                        <li className="Carousel-ListItem" key={num}>{item}</li>;
                    })}
                </ul>
            </div>
        );
    }
}

export default Carousel;
