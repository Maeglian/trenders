import React from 'react';
import classnames from 'classnames';
import Title from '../Title/Title';
import {ReactComponent as Close} from '../../images/svg/close.svg';
import {ReactComponent as Undo} from '../../images/svg/undo.svg';
import Icon from '../Icon/Icon';
import './Carousel.scss';


interface CarouselProps {
    title?: string;
    margin: string;
    carouselId?: string;
    canBeHidden: boolean;
    children: unknown;
}

interface CarouselState {
    isHidden: boolean;
}

class Carousel extends React.Component<CarouselProps, CarouselState> {
    public static defaultProps = {
        margin: 'm',
        canBeHidden: true,
    };
    public state = {
        isHidden: false,
    };
    public handleHide = () => {
        this.setState((state) => ({
            isHidden: !state.isHidden,
        }));
    }
    public render() {
        const { children, margin, title, carouselId, canBeHidden } = this.props;
        const { isHidden } = this.state;
        const itemCn = classnames(
            'Carousel-Item',
            margin && `Carousel-Item_margin_${margin}`,
        );
        const titleCn = classnames(
            'Carousel-TitleWrapper',
            isHidden && 'Carousel-TitleWrapper_hidden',
        );
        const url = carouselId && `https://yandex.ru/efir?from=efir_touch&stream_active=theme&stream_publisher=${carouselId}`;

        return (
            <div className="Carousel">
                {canBeHidden && <div className="Carousel-Header">
                    <div className={titleCn}>
                        {title && <Title url={url}>{title}</Title>}
                        {isHidden &&
                            <div className="Carousel-HideInfo">Вы скрыли подборку видео из ленты</div>}
                    </div>
                    <Icon className="Carousel-Hide">
                        {!isHidden && <Close width="13" height="13" viewBox="0 0 16 16" onClick={this.handleHide}/>}
                        {isHidden && <Undo width="17" height="17" viewBox="2 0 18 17" onClick={this.handleHide}/>}
                    </Icon>
                </div>}
                {!isHidden && <div className="Carousel-List">
                    {React.Children.map(children, (child, num) =>
                        <div className={itemCn} key={num}>{child}</div>)}
                </div>}
            </div>
        );
    }
}

export default Carousel;
