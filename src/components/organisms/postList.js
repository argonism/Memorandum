import React, { Fragment } from "react";
import PostListItem from "components/molecules/postListItem";
import Pagination from "components/molecules/pagination";

const PostList = ({ data, page, path, pageListSize }) => {
    const posts = data.filter((post) => {
        return !post.node.frontmatter.draft;
    });
    console.log(posts);
    return (
        <Fragment>
            {posts.map(({ node }) => {
                return <PostListItem key={node.fields.slug} node={node} />;
            })}
            {page && (
                <Pagination page={page} path={path} listSize={pageListSize} />
            )}
        </Fragment>
    );
};

export default PostList;
