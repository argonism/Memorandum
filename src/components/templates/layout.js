import React, { Fragment } from "react";
import styled, {
    css,
    createGlobalStyle,
    ThemeProvider,
} from "styled-components";
import lightTheme from "themes/light";
import darkTheme from "themes/dark";
// import { local, getItem, setItem } from "utils/storage";
// import ThemeSwitch from "components/molecules/themeSwitch";
import SideHeader from "components/organisms/sideHeader";
import SideContent from "components/organisms/sideContent";
import SideFooter from "components/organisms/sideFooter";
import MainHeader from "components/organisms/mainHeader";
import MainContent from "components/organisms/mainContent";

const GlobalStyle = createGlobalStyle`
    * {
        margin: 0;
        padding: 0;

        a {
            text-decoration: none;
            &:hover {
                text-decoration: none;
            }
        }
    }
    html, body {
        overflow: auto;
        background-color: ${(props) => props.theme.main.defaultBack};

        ${(props) =>
            props.mobileOpen &&
            css`
                overflow: hidden;
                position: fixed;
                width: 100%;
                height: 100%;
            `}
            
        div[role='group'] {
            /* iphone의 elastic scrolling 시, 고정된 헤더가 가려지지 않도록 body 에 속해있던 속성을 하단 div로 가져옴 */
            -webkit-overflow-scrolling: touch;
        }
    }
`;

const SideBar = styled.div`
    max-width: 280px;
    height: 100vh;
    z-index: 3;

    background-color: ${(props) => props.theme.side.defaultBack};
    color: ${(props) => props.theme.side.defaultText} !important;

    transition: margin 0.5s;
    margin-left: ${(props) => (props.mobileOpen ? 0 : "-281px")};
    position: fixed;
    top: 0;
    height: 100vh;

    @media all and (max-width: 992px) {
        position: auto;
        top: auto;
    }
    @media all and (min-width: 992px) {
        min-width: 280px;
        margin-left: 0 !important;
    }
`;

const Main = styled.div`
    margin-top: ${(props) => (props.mobileOpen ? 0 : "50px")};
    max-width: 920px;

    margin-left: 0;
    color: ${(props) => props.theme.main.defaultText} !important;

    @media all and (min-width: 992px) {
        margin-top: 0;
        margin-left: 280px !important;
    }
`;

const MainOverlay = styled.div`
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background-color: ${(props) => props.theme.main.overlayBack};
    opacity: 0.8;

    z-index: 2;

    @media all and (min-width: 992px) {
        display: none;
    }
`;

const Wrapper = styled.div`
    display: flex;
    flex-direction: row;
    max-width: 1200px;
    margin: auto;
`;

const SideBarWrapper = styled.div`
    /* position: fixed;
    top: 0;
    height: 100vh;

    @media all and (max-width: 992px) {
        position: auto;
        top: auto;
    } */
`;

export default class Layout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            mobile_side: false,
            isDarkMode: false,
        };
    }

    sideToggle = (e) => {
        const open = !this.state.mobile_side;
        this.setState({
            mobile_side: open,
        });
    };

    render() {
        const { children, activeMenu } = this.props;
        const { mobile_side, isDarkMode } = this.state;
        return (
            <ThemeProvider theme={isDarkMode ? darkTheme : lightTheme}>
                <Wrapper>
                    <GlobalStyle mobileOpen={mobile_side} />
                    <SideBar mobileOpen={mobile_side}>
                        <SideBarWrapper>
                            <SideHeader />
                            <SideContent activeMenu={activeMenu} />
                            <SideFooter>
                                {/* <ThemeSwitch
                                    onChange={this.themeToggle}
                                    checked={isDarkMode}
                                /> */}
                            </SideFooter>
                        </SideBarWrapper>
                    </SideBar>
                    <Main>
                        {mobile_side && (
                            <MainOverlay onClick={this.sideToggle} />
                        )}
                        <MainHeader sideToggle={this.sideToggle} />
                        <MainContent>{children}</MainContent>
                    </Main>
                </Wrapper>
            </ThemeProvider>
        );
    }
}
