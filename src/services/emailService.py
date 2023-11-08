
# class SendGridLib
# {   

#     protected  $url = SENDG;
    
#     public function __construct()
#     {
#         $this->ci =& get_instance();
#     }
#     /**
#      * Metodo para consumir SendGrid desde Bitinka
#      * @author Gustavo Pino
#      * @date 11-01-2017
#      *
#      * @url http://192.168.5.108:5000/api/v1/mail
#      * @method POST
#      * @params $to, $toname, $from, $fromname, $replyto, $cc, $ccname, $bcc, $bccname, $subject, $text, $msj
#      *
#      * $to
#      * $toname
#      * $from
#      * $fromname
#      * $replyto
#      * $cc
#      * $ccname
#      * $bcc
#      * $bccname
#      * $subject
#      * $text
#      * $msj
#      *
#      */

#     public function envio_email($to, $toname, $from, $fromname, $replyto = 0, $cc = 0, $ccname = 0, $bcc = 0, $bccname = 0, $subject, $text, $msj)
#     {

#         $this->ci->load->library('rest');
#         $this->ci->rest->initialize(array('server'   => $this->url));
#         $arreglo = [
#             'to'        =>      $to,
#             'toname'    =>      $toname,
#             'from'      =>      $from,
#             'fromname'  =>      $fromname,
#             'replyto'   =>      $replyto,
#             'cc'        =>      $cc,
#             'ccname'    =>      $ccname,
#             'bcc'       =>      $bcc,
#             'bccname'   =>      $bccname,
#             'subject'   =>      $subject,
#             'html'      =>      $msj,
#             'text'      =>      $text,
#             'client'    =>      'Bitinka'
#         ];

#         if($cc != 0){
#             array_push($arreglo,['ccname' => $ccname],['cc' => $cc]);
#         }
#         if($bcc != 0){
#             array_push($arreglo,['bccname' => $bccname], ['bcc' => $bcc]);
#         }
#         if($replyto != 0){
#             array_push($arreglo,['replyto' => $replyto]);
#         }
#         $curl = curl_init();
#         curl_setopt_array($curl, array(
#           CURLOPT_URL => $this->url.'/api/v1/mail',
#           CURLOPT_RETURNTRANSFER => true,
#           CURLOPT_ENCODING => '',
#           CURLOPT_MAXREDIRS => 10,
#           CURLOPT_TIMEOUT => 0,
#           CURLOPT_FOLLOWLOCATION => true,
#           CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
#           CURLOPT_CUSTOMREQUEST => 'POST',
#           CURLOPT_POSTFIELDS => $arreglo,
#           ));
#         $response = curl_exec($curl);
#         curl_close($curl);
#         #var_dump($response);
#         //$this->ci->rest->post("/api/v1/mail", $arreglo, '');
#         //$respuesta=$this->ci->rest->post("/api/v1/mail", $arreglo);
#     }
# }
