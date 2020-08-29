const theme_color = "#fff";
const text_color = "#454545";

export default {
    main: {
        defaultBack: "#fff",
        defaultText: text_color,
        overlayBack: text_color,
        header: {
            back: theme_color,
            text: "#fff",
            button: "#fff",
        },
    },
    side: {
        defaultBack: theme_color,
        defaultText: text_color,
        bio: {
            circle: "#49c39e",
            defaultText: "#999",
            activeText: text_color,
        },
        category: {
            activeText: "#fff",
            activeBack: "#49c39e",
        },
    },
    bio: {
        defaultBack: "#fff",
        defaultText: text_color,
        subText: "#999",
        socialButton: "#000",
    },
    postlistitem: {
        title: "#000",
        content: "#999",
        info: "#000",
    },
    pagination: {
        defaultText: "#999",
        activeText: text_color,
        activeBack: theme_color,
    },
    blogpost: {
        title: text_color,
        info: "#999",
        hr: "#999",
        content: {
            default: "#000",
            quote: "#999",
            link: "#0687f0",
        },
    },
    tag: {
        back: "#d9d9d9",
        text: "#4d4d4d",
    },
    recentpostlist: {
        header: "#000",
        category: "#0687f0",
    },
    recentpostitem: {
        text: "#fff",
    },
};
