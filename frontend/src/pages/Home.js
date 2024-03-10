import '../css/home.css';
import laptop_icon from '../images/laptop-icon.png';


export default function Home() {

    return (
        <div>
            {/* <a id="hero" class="anchor"></a> */}
            <div id="section-hero" className="section-body">
                <img src={laptop_icon}/>
                <h2 id="aaron" className="title">Aaron Tran</h2>
                <h4 id="education">4th Year Software Engineer/Commerce Student</h4>
            </div>
        
        </div>
    )
}