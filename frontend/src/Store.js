import React from 'react';
import { Icon, Layout, Breadcrumb, Button, Menu, List, Avatar } from 'antd';
const { Header, Content, Footer, Sider } = Layout;

class Store extends React.Component {
    state = {
        collapsed: false,
    };

    render() {
        const IconText = ({ type, text }) => (
            <span>
                <Icon type={type} style={{ marginRight: 8 }} />
                {text}
            </span>
        );
        const listData = [];
        for (let i = 0; i < 23; i++) {
            listData.push({
                href: 'http://ant.design',
                title: `ant design part ${i}`,
                description:
                    'Ant Design, a design language for background applications, is refined by Ant UED Team.',
                content:
                    'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
            });
        }

        return (

            <Content style={{ margin: '0 16px' }}>
                <Breadcrumb style={{ margin: '16px 0' }}>
                    <Breadcrumb.Item>User</Breadcrumb.Item>
                    <Breadcrumb.Item>Bill</Breadcrumb.Item>
                </Breadcrumb>

                <Layout>
                    <Sider theme="light" collapsible collapsed={this.state.collapsed} onCollapse={this.onCollapse}>

                        <Button type="primary" block onClick={() => { this.setState({ collapsed: !this.state.collapsed }) }} style={{ marginBottom: 16 }}>
                            <Icon type={this.state.collapsed ? 'right' : 'left'} />
                        </Button>
                        <Menu mode="inline" selectedKeys={['2']}>
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
                            dataSource={listData}
                            footer={
                                <></>
                            }
                            renderItem={item => (
                                <List.Item
                                    key={item.title}
                                    actions={[
                                        <IconText type="star-o" text="156" />,
                                        <IconText type="like-o" text="156" />,
                                        <IconText type="message" text="2" />,
                                    ]}
                                    extra={
                                        <img
                                            width={272}
                                            alt="logo"
                                            src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
                                        />
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