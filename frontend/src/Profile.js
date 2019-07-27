import React from 'react';
import './App.css';
import { Card, Descriptions } from 'antd';


class Profile extends React.Component {
    componentWillMount() {
        fetch('')
        .then(response => response.json() )
        .then()
    }
    render() {
        return (
        <Card title="Card title" hoverable	 bordered={false} style={{ width: '50%', margin: 'auto' }}>
        <Descriptions title="User Info" bordered>
        <Descriptions.Item label="UserName">Zhou Maomao</Descriptions.Item>
        <Descriptions.Item label="Telephone">1810000000</Descriptions.Item>
        <Descriptions.Item label="Live">Hangzhou, Zhejiang</Descriptions.Item>
        <Descriptions.Item label="Remark">empty</Descriptions.Item>
        <Descriptions.Item label="Address">
        No. 18, Wantang Road, Xihu District, Hangzhou, Zhejiang, China
        </Descriptions.Item>
        </Descriptions>
        </Card>)
    }

}

export default Profile;