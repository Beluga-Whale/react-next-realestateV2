import React from 'react'
import Link from 'next/link'
import Image from 'next/image'
import { Link as LinkS, animateScroll as scroll } from 'react-scroll'

const Footer = () => {
    const toggleHome = () => {
        scroll.scrollToTop()
    }
    return (
        <div id='footer' className='footer-container'>
            <div className="footer-wrapper ">
                <div className="footer-items ">
                    <h1 className='font-bold my-4'>About Us</h1>
                    <Link href="/"><a>How it works</a></Link>
                    <Link href="/"><a>Testimonials</a></Link>
                    <Link href="/"><a>Carees</a></Link>
                    <Link href="/"><a>Terms of Services</a></Link>
                </div>
                <div className="footer-items ">
                    <h1 className='font-bold my-4'>Videos</h1>
                    <Link href="/"><a>Submit Video</a></Link>
                    <Link href="/"><a>Ambassador</a></Link>
                    <Link href="/"><a>Agency</a></Link>
                    <Link href="/"><a>Infuence</a></Link>
                </div>
                <div className="footer-items">
                    <h1 className='font-bold my-4'>Contact Us</h1>
                    <Link href="/"><a>Contact</a></Link>
                    <Link href="/"><a>Support</a></Link>
                    <Link href="/"><a>Destination</a></Link>
                    <Link href="/"><a>Sponsorships</a></Link>
                </div>
                <div className="footer-items">
                    <h1 className='font-bold my-4'>Social Media</h1>
                    <Link href="/"><a>Instagram</a></Link>
                    <Link href="/"><a>Facebook</a></Link>
                    <Link href="/"><a>Youtube</a></Link>
                    <Link href="/"><a>Twitter</a></Link></div>
            </div>

            <div className="footer-bottom ">
                <LinkS to="/"
                    onClick={toggleHome}
                    className="hover:animate-bounce cursor-pointer"
                    smooth={true}
                    duration={500}
                    spy={true}
                    exact='true'
                    offset={-220}
                >
                    <Image src={'/Logo.svg'} alt="Logo" width={130} height={35} />
                </LinkS>
                <div>
                    <span>&copy; 2022 All rights reserved.</span>
                    <div className='footer-socials'>
                        <Link href="/">
                            <a className='hover:animate-bounce duration-300'>
                                <Image src={'/Facebook.svg'} width={24} height={24} />
                            </a>
                        </Link>
                        <Link href="/">
                            <a className='hover:animate-bounce duration-300'>
                                <Image src={'/Twitter.svg'} width={24} height={24} />
                            </a>
                        </Link>
                        <Link href="/">
                            <a className='hover:animate-bounce duration-300'>
                                <Image src={'/Instagram.svg'} width={24} height={24} />
                            </a>
                        </Link>
                        <Link href="/">
                            <a className='hover:animate-bounce duration-300'>
                                <Image src={'/Youtube.svg'} width={24} height={24} />
                            </a>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Footer