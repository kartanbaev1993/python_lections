--
-- PostgreSQL database dump
--

-- Dumped from database version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: blogger; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.blogger (
    id integer NOT NULL,
    name character varying(50)
);


ALTER TABLE public.blogger OWNER TO "user";

--
-- Name: blogger_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.blogger_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blogger_id_seq OWNER TO "user";

--
-- Name: blogger_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.blogger_id_seq OWNED BY public.blogger.id;


--
-- Name: post; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.post (
    id integer NOT NULL,
    blogger_id integer,
    body text,
    created_at date
);


ALTER TABLE public.post OWNER TO "user";

--
-- Name: post_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.post_id_seq OWNER TO "user";

--
-- Name: post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.post_id_seq OWNED BY public.post.id;


--
-- Name: blogger id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.blogger ALTER COLUMN id SET DEFAULT nextval('public.blogger_id_seq'::regclass);


--
-- Name: post id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.post ALTER COLUMN id SET DEFAULT nextval('public.post_id_seq'::regclass);


--
-- Data for Name: blogger; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.blogger (id, name) FROM stdin;
1	blogger 1
2	blogger 2
3	blogger 3
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.post (id, blogger_id, body, created_at) FROM stdin;
1	1	my first blog	2020-08-01
2	1	today is a good day	2020-09-02
3	1	it is my b-day!	2021-09-30
4	2	my first post	2013-05-10
5	2	some post	2022-06-23
6	3	i am not a blogger	2022-08-15
\.


--
-- Name: blogger_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.blogger_id_seq', 3, true);


--
-- Name: post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.post_id_seq', 6, true);


--
-- Name: blogger blogger_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.blogger
    ADD CONSTRAINT blogger_pkey PRIMARY KEY (id);


--
-- Name: post post_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (id);


--
-- Name: post fk_post_blogger; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT fk_post_blogger FOREIGN KEY (blogger_id) REFERENCES public.blogger(id);


--
-- PostgreSQL database dump complete
--

