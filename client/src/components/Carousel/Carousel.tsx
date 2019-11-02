import React from 'react';
import ReactDOM from 'react-dom';
import './Carousel.scss';

interface CarouselProps {
    title: string;
    children: unknown;
}

class Carousel extends React.Component<CarouselProps> {
    public static defaultProps = {
        title: '',
    };
    public render() {
        const children = this.props.children;
        return (
            <div className="Carousel">
                <div className="Carousel-Header">
                    <div className="Carousel-HeaderTitle">{this.props.title}</div>
                    <div className="Carousel-HeaderHide"></div>
                </div>
                <div className="Carousel-List">
                    {React.Children.map(children, (child, num) =>
                        <div className="Carousel-ListItem" key={num}>{child}</div>)}
                </div>
            </div>
        );
    }
}

export default Carousel;
