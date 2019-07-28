import React from 'react';
import { Tag, Icon, Layout, Breadcrumb, Button, Menu, List, Avatar } from 'antd';
import cookie  from "react-cookies";

const { Header, Content, Footer, Sider } = Layout;

class Store extends React.Component {
    state = {
        collapsed: false,
        listData: []
    };
    PurchaseItem = (id) => {
        const data = {
            itemID: id,
            userID: cookie.load('userID')
        }
        fetch('http://localhost:5000/purchaseItems', {
            
            method: 'POST',
            body: JSON.stringify(data),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },
        })
        .then(response => response.json() )
        .then(j => {
            if (j.status === 200){
                window.location.href = '/';
            } 
        })
    }
    onSearch = (value) => {
        const data = {input: value}
        fetch('http://localhost:5000/search', {
            
            method: 'POST',
            body: JSON.stringify(data),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },
        })
        .then(response => response.json() )
        .then(j => {
            console.log(JSON.stringify(j));
            let data = [];
            for (let item of j){
                data.push({
                    id: item['itemID'],
                    title: item['itemName'],
                    description:
                        item['userName'],
                    content:
                        item['itemDescription'],
                    score:
                        item['score'],

                });
            }
            this.setState({ listData: data})
        
        })
    }
    componentDidMount() {
        let params = new URLSearchParams(this.props.location.search);
        const search = params.get('search')
        if (search){
            this.onSearch(search)
        } else {
            fetch('http://localhost:5000/items')
            .then(response => response.json())
            .then(j => {
                let data = [];
                for (let item of j){
                    data.push({
                        id: item['itemID'],
                        price: item['price'],
                        title: item['itemName'],
                        description:
                            item['userName'],
                        content:
                            item['itemDescription'],
                        score:
                            item['score'],

                    });
                }
                this.setState({ listData: data})
            
            })
        }
    }
    render() {
        
        const IconText = ({ type, text }) => (
            <span>
                <Icon type={type} style={{ marginRight: 8 }} />
                {text}
            </span>
        );
        
        return (

            <Content style={{ margin: '0 16px' }}>
                <Breadcrumb style={{ margin: '16px 0' }}>
                    <Breadcrumb.Item>Buy</Breadcrumb.Item>
                    <Breadcrumb.Item>Food</Breadcrumb.Item>
                </Breadcrumb>

                <Layout>
                    <Sider theme="light" collapsible collapsed={this.state.collapsed} onCollapse={this.onCollapse}>

                        <Button type="primary" block onClick={() => { this.setState({ collapsed: !this.state.collapsed }) }} style={{ marginBottom: 16 }}>
                            <Icon type={this.state.collapsed ? 'right' : 'left'} />
                        </Button>
                        <Menu mode="inline" selectedKeys={['1']}>
                            <Menu.Item key="1">
                                <Icon type="coffee" />
                                <span>Food</span>
                            </Menu.Item>
                            <Menu.Item key="2">
                                <Icon type="skin" />
                                <span>Clothes</span>
                            </Menu.Item>
                            <Menu.Item key="4">
                                <Icon type="home" />
                                <span>Shelter</span>
                            </Menu.Item>
                            <Menu.Item key="5">
                                <Icon type="laptop" />
                                <span>Jobs</span>
                            </Menu.Item>
                        </Menu>
                    </Sider>
                    <Content style={{ marginLeft: "10px" }}>



                        <List
                            itemLayout="vertical"
                            size="large"
                            pagination={{
                                onChange: page => {
                                    console.log(page);
                                },
                                pageSize: 5,
                            }}
                            dataSource={this.state.listData}
                            footer={
                                <></>
                            }
                            renderItem={item => (
                                <List.Item
                                    key={item.title}
                                    actions={[
                                        <IconText type="star-o" text={item.score} />,
                                        <Tag color='geekblue'>
                                            {item.price === 0 ? 'Free!' : '$' + item.price}
                                        </Tag>,
                                        <Button type="primary" onClick={() => this.PurchaseItem(item.id)}>Purchase</Button>
                                    ]}
                                    extra={ item.img ? <img
                                        width={272}
                                        alt="logo"
                                        src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
                                    /> : null 
                                       
                                    }
                                >
                                    <List.Item.Meta
                                        avatar={item.avatar ? <Avatar src={item.avatar} /> : <Avatar icon="user" />}
                                        title={<a href={item.href}>{item.title}</a>}
                                        description={item.description}
                                    />
                                    {item.content}
                                </List.Item>
                            )}
                        />

                    </Content>
                </Layout>
            </Content>

        );
    }
}

export default Store;