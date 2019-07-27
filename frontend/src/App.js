import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Button, Layout, Menu, Breadcrumb, List, Avatar, Icon, Modal, Form, Input, Checkbox } from 'antd';
import { withRouter, BrowserRouter as Router, Route, Link } from "react-router-dom";
import LoginForm from "./LoginForm.js";
import Store  from "./Store.js";
import Sell  from "./Sell.js";
const { Header, Content, Footer, Sider } = Layout;
const { SubMenu } = Menu;


class Cart extends React.Component {
    render() {
        return (<></>);
    }
}


class App extends React.Component {
    state = {
        login: false,
        activePage: "home"
    };
  
    MenuOnClick = ({item, keyPath}) => {
        if (keyPath[0] === "login") {
            this.setState({
                login: true
            })
        } else {
            this.setState({
                activePage: keyPath[0]
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
        const MainMenu = withRouter(props => {
            const { location } = props
            return (
            <Menu theme="dark" defaultSelectedKeys={[location.pathname]} mode="horizontal"
                onClick={this.MenuOnClick}
                style={{ lineHeight: '64px' }}>
                <Menu.Item key="/store"
                    //style={{ float: 'left' }}
                    >
                    <Link to="/store"> 
                        <Icon type="shopping" />
                        <span>Buy</span>
                    </Link>
                </Menu.Item>
                <Menu.Item key="/sell"
                    //style={{ float: 'left' }}
                    >
                    <Link to="/sell"> 
                        <Icon type="dollar" />
                        <span>Sell / Donate</span>
                    </Link>
                </Menu.Item>
                <Menu.Item
                    //style={{ float: 'left' }}
                    key="/cart">
                    <Link to="/cart"> 
                        <Icon type="shopping-cart" />
                        <span>Cart</span>
                    </Link>
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
            });
        return (
            <Router>
                <Layout style={{ minHeight: '100vh' }}>

                    <Header  >
                        <div className="logo" />
                        <MainMenu />
                    </Header>
                    <Layout>

                        <Route path="/store" component={Store} />
                        <Route path="/sell" component={Sell} />
                        <Route path="/cart" component={Cart} />
                        <Footer style={{ textAlign: 'center' }}> </Footer>
                    </Layout>

                </Layout>
            </Router>
        );
    }
}

export default App;
