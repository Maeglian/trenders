import React from 'react';
import { State } from '../../store/createStore';
import { connect } from 'react-redux';
import './Channels.scss';

interface Channel {
    channelId: string;
    title: string;
}

interface ChannelProps {
    channels: Channel[];
}

class Channels extends React.Component<ChannelProps> {
    public render() {
        const { channels } = this.props;

        return (<div className="Channels">
            {channels.map((channel, num) => {
                const { channelId, title } = channel;
                const url = `https://yandex.ru/efir?stream_channel=${channelId}%26from=efir`;
                const iconUrl = "url('https://avatars.mds.yandex.net/get-vh/2441592/2a0000016e457a9bcf803389abf674a2cb2d/orig')";

                return (
                    <div className="Channels-Item">
                        <div className="Channels-Icon" style={{ backgroundImage: iconUrl, backgroundPosition: '26.565% 0' }}></div>
                        <a className="Channels-Link" href={url} key={num}>{title}</a>
                    </div>
                );
            })}
        </div>);
    }
}

const mapStateToProps = (state: State) => ({
    channels: state.channels,
});

export default connect(mapStateToProps)(Channels);
