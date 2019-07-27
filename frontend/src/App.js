import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Button, Layout, Menu, Breadcrumb, List, Avatar, Icon, Modal, Form, Input, Checkbox } from 'antd';
import { Switch, Route, Redirect, withRouter, BrowserRouter as Router, Link } from "react-router-dom";
import cookie  from "react-cookies";
import LoginForm from "./LoginForm.js";
import Store  from "./Store.js";
import Sell  from "./Sell.js";
import Profile  from "./Profile.js";
import PurchaseHistory  from "./History.js";
import Register  from "./Register.js";

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
        activePage: "/"
    };
  
    componentWillMount() {
        this.setState(  { username: cookie.load('username'), userID: cookie.load('userID') } );
    }
    
    MenuOnClick = ({item, keyPath}) => {
        if (keyPath[0] === "/login") {
            this.setState({
                login: true
            })
        } else if (keyPath[0] === "/logout") {
            this.setState({username: cookie.load('username'), userID: cookie.load('userID') }) 

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
        const Logout = () => {
            cookie.remove('userID', { path: '/' })
            return (<Redirect to='/'></Redirect>)
        }
        const ItemMenu = (props) => {
            const {idx, icon, text} = props;
            
            return (
            <Menu.Item {...props}
            >
            <Link to={idx}> 
                <Icon type={icon} />
                <span>{text}</span>
            </Link>
            </Menu.Item>
            );
        }
        const MainMenu = withRouter(props => {
            const { location } = props
            return (
            <Menu theme="dark" defaultSelectedKeys={[location.pathname]} mode="horizontal"
                onClick={this.MenuOnClick}
                style={{ lineHeight: '64px' }}>
                <ItemMenu idx="/store" key="/store" icon="shopping" text="Buy" />
                <ItemMenu idx="/sell" key="/sell" icon="dollar" text="Sell / Donate" />
                <ItemMenu idx="/cart" key="/cart" icon="shopping-cart" text="Cart" />
                { this.state.userID ? 
            
                <SubMenu key="profile"
                    title={

                        <span>
                            <Icon type="user" />
                            <span>{this.state.username.charAt(0).toUpperCase() + this.state.username.slice(1)}</span>
                        </span>
                    }
                    >
                    <ItemMenu idx="/profile"   key="/profile"   icon="idcard" text="Profile" />
                    <ItemMenu idx="/history"   key="/history"   icon="history" text="Purchase History" />
                    <ItemMenu idx="/userItems" key="/userItems" icon="dollar" text="Listed items" />
                    <ItemMenu idx="/logout" key="/logout" icon="logout" text="Logout" />
                </SubMenu>
                :
                <ItemMenu idx="/login" key="/login" icon="login" text="Login" />
            }
                <Modal
          title="Login form"
          visible={this.state.login}
          onOk={this.handleOk}
          onCancel={() => {this.setState({login: false})}}
        >
            <LoginForm onCancel={() => {
                this.setState({login: false, username: cookie.load('username'), userID: cookie.load('userID') }) 

                }}></LoginForm>
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
                        <Switch>
                            <Route exact path="/" render={() => {
                                this.setState({ activePage: "/store"})
                                return (
                                <Redirect to="/store" />
                            );}} />
                            <Route path="/store" component={Store} />
                            <Route path="/sell" component={Sell} />
                            <Route path="/cart" component={Cart} />
                            <Route path="/profile" component={Profile} />
                            <Route path="/history" component={PurchaseHistory} />
                            <Route path="/register" component={Register} />
                            <Route path="/logout" component={Logout}/>
                            {/* <Route path="/userItems" component={UserItems} /> */}
                        </Switch>

                        <Footer style={{ textAlign: 'center' }}> </Footer>
                    </Layout>

                </Layout>
            </Router>
        );
    }
}

export default App;
