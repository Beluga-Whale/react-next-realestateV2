import React from 'react'
import Link from 'next/link'

const SideBar = () => {
    return (
        <div>
            <section className="sidebar">
                <Link href="/CountryAll/AmericaHome/">
                    <a>America</a>
                </Link>
                <Link href="/CountryAll/SpainHome/">
                    <a>Spain</a>
                </Link>
                <Link href="/CountryAll/LondonHome/">
                    <a>London</a>
                </Link>
                <Link href="/CountryAll/FranceHome/">
                    <a>France</a>
                </Link>
            </section>
        </div>
    )
}

export default SideBar