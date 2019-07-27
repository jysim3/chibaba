import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Button, Layout, Menu, Breadcrumb, List, Avatar, Icon, Modal, Form, Input, Checkbox } from 'antd';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import LoginForm from "./LoginForm.js";
import Store  from "./Store.js";
import Sell  from "./Sell.js";
const { Header, Content, Footer, Sider } = Layout;
const { SubMenu } = Menu;




class App extends React.Component {
    state = {
        login: false
    };
  
    MenuOnClick = ({item, keyPath}) => {
        if (keyPath[0] === "login") {
            console.log("jsdafjkl");
            this.setState({
                login: true
            })
        }

    }
    handleOk = e => {
        console.log(e);
        this.setState({
            login: false
        })
    }

    render() {
        const MainMenu = () => (
            <Menu theme="dark" defaultSelectedKeys={['1']} mode="horizontal"
                onClick={this.MenuOnClick}
                style={{ lineHeight: '64px' }}>
                <Menu.Item key="1"
                    //style={{ float: 'left' }}
                    >
                    <Icon type="shopping" />
                    <span>Buy</span>
                </Menu.Item>
                <Menu.Item key="2"
                    //style={{ float: 'left' }}
                    >
                    <Icon type="dollar" />
                    <span>Sell / Donate</span>
                </Menu.Item>
                <Menu.Item
                    //style={{ float: 'left' }}
                    key="9">
                    <Icon type="shopping-cart" />
                    <span>Cart</span>
                </Menu.Item>
                <Menu.Item
                    //style={{ float: 'left' }}
                    key="login">
                        <span>
                            <Icon type="user" />
                            <span>Login</span>
                        </span>
                    
    
                </Menu.Item>
                <Modal
          title="Login form"
          visible={this.state.login}
          onOk={this.handleOk}
          onCancel={() => {this.setState({login: false})}}
        >
            <LoginForm></LoginForm>
      </Modal>
            </Menu>
        );
        return (
            <Router>
                <Layout style={{ minHeight: '100vh' }}>

                    <Header  >
                        <div className="logo" />
                        <MainMenu />
                    </Header>
                    <Layout>

                        <Route path="/store" component={Store} />

                        <Footer style={{ textAlign: 'center' }}>Lmao footer </Footer>
                    </Layout>

                </Layout>
            </Router>
        );
    }
}

export default App;
