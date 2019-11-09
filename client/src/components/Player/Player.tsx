import React from 'react';
import { ReactComponent as Like } from '../../images/svg/like.svg';
import { ReactComponent as Next } from '../../images/svg/next.svg';
import { State } from '../../store/createStore';
import { connect } from 'react-redux';
import './Player.scss';


interface PlayerProps {
    content: any;
}

class Player extends React.Component<PlayerProps> {
    public render() {
        const { content } = this.props;
        const playerContent = content[5].includes[0];
        const { content_url: url, thumbnail: preview, title, blogger } = playerContent;
        const src = `https://yastatic.net/yandex-video-player-iframe-api/index.html?stream_url=${url}&preview=${preview}`;

        return (
            <div className="Player">
                <div className="Player-Container">
                    <iframe title="Player" src={src} style={{ width: '100%', height: '100%', border: 'none' }}></iframe>
                </div>
                <div className="Player-Info">
                    {blogger && <img className="Player-Avatar"src={blogger.avatar} alt="avatar"/>}
                    <div className="Player-Text">
                        <div className="Player-Title">{title}</div>
                        {blogger && <div className="Player-Channel">{blogger.title}</div>}
                    </div>
                    <div className="Player-Controls">
                        <div className="Player-Icon Player-Icon_like">
                            <Like width="16px" height="16px"/>
                        </div>
                        <div className="Player-Icon Player-Icon_dislike">
                            <Like width="16px" height="16px"/>
                        </div>
                        <div className="Player-Icon Player-Icon_next">
                            <Next />
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

const mapStateToProps = (state: State) => ({
    content: state.main,
});

export default connect(mapStateToProps)(Player);
