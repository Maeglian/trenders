import React from 'react';
import classnames from 'classnames';
import Title from '../Title/Title';
import './Carousel.scss';


interface CarouselProps {
    title?: string;
    margin: string;
    carouselId?: string;
    ableToBeHidden: boolean;
    children: unknown;
}

interface CarouselState {
    isHidden: boolean;
}

class Carousel extends React.Component<CarouselProps, CarouselState> {

    public static defaultProps = {
        margin: 'm',
        ableToBeHidden: true,
    };
    constructor(props: CarouselProps) {
        super(props);
        this.state = {
            isHidden: false,
        };
        this.close = this.close.bind(this);
    }
    public close() {
        this.setState((state) => ({
            isHidden: !state.isHidden,
        }));
    }    public render() {
        const { children, margin, title, carouselId, ableToBeHidden } = this.props;
        const itemCn = classnames(
            'Carousel-Item',
            margin && `Carousel-Item_margin_${margin}`,
        );
        const hideCn = classnames(
            'Carousel-Hide',
            this.state.isHidden && 'Carousel-Hide_hidden',
        );
        const titleCn = classnames(
            'Carousel-TitleWrapper',
            this.state.isHidden && 'Carousel-TitleWrapper_hidden',
        );
        const url = carouselId
                    ? `https://yandex.ru/efir?from=efir_touch&stream_active=theme&stream_publisher=${carouselId}`
                    : undefined;

        return (
            <div className="Carousel">
                {ableToBeHidden && <div className="Carousel-Header">
                    <div className={titleCn}>
                        {title && <Title url={url}>{title}</Title>}
                        {this.state.isHidden &&
                            <div className="Carousel-HideInfo">Вы скрыли подборку видео из ленты</div>}
                    </div>
                    <div className={hideCn} onClick={this.close}></div>

                </div>}
                {!this.state.isHidden && <div className="Carousel-List">
                    {React.Children.map(children, (child, num) =>
                        <div className={itemCn} key={num}>{child}</div>)}
                </div>}
            </div>
        );
    }
}

export default Carousel;
